#!/usr/bin/env python
#
# Author: Mike McKerns (mmckerns @caltech and @uqfoundation)
# Author: Leonardo Gama (@leogama)
# Copyright (c) 2008-2015 California Institute of Technology.
# Copyright (c) 2016-2024 The Uncertainty Quantification Foundation.
# License: 3-clause BSD.  The full license text is available at:
#  - https://github.com/uqfoundation/dill/blob/master/LICENSE
"""
Pickle and restore the intepreter session.
"""

__all__ = [
    'dump_module', 'load_module', 'load_module_asdict',
    'dump_session', 'load_session' # backward compatibility
]

import os
import pathlib
import re
import sys
import tempfile
import warnings

TEMPDIR = pathlib.PurePath(tempfile.gettempdir())

# Type hints.
from typing import Optional, Union

from prophecy.utils.dill import _dill, Pickler, Unpickler

from ._dill import (
    BuiltinMethodType, FunctionType, MethodType, ModuleType, TypeType,
    _import_module, _is_builtin_module, _is_imported_module, _main_module,
    _reverse_typemap, __builtin__, UnpicklingError,
)

def _module_map():
    """get map of imported modules"""
    from collections import defaultdict
    from types import SimpleNamespace
    modmap = SimpleNamespace(
        by_name=defaultdict(list),
        by_id=defaultdict(list),
        top_level={},
    )
    for modname, module in sys.modules.items():
        if modname in ('__main__', '__mp_main__') or not isinstance(module, ModuleType):
            continue
        if '.' not in modname:
            modmap.top_level[id(module)] = modname
        for objname, modobj in module.__dict__.items():
            modmap.by_name[objname].append((modobj, modname))
            modmap.by_id[id(modobj)].append((modobj, objname, modname))
    return modmap

IMPORTED_AS_TYPES = (ModuleType, TypeType, FunctionType, MethodType, BuiltinMethodType)
if 'PyCapsuleType' in _reverse_typemap:
    IMPORTED_AS_TYPES += (_reverse_typemap['PyCapsuleType'],)
IMPORTED_AS_MODULES = ('ctypes', 'typing', 'subprocess', 'threading',
                               r'concurrent\.futures(\.\w+)?', r'multiprocessing(\.\w+)?')
IMPORTED_AS_MODULES = tuple(re.compile(x) for x in IMPORTED_AS_MODULES)

def _lookup_module(modmap, name, obj, main_module):
    """lookup name or id of obj if module is imported"""
    for modobj, modname in modmap.by_name[name]:
        if modobj is obj and sys.modules[modname] is not main_module:
            return modname, name
    __module__ = getattr(obj, '__module__', None)
    if isinstance(obj, IMPORTED_AS_TYPES) or (__module__ is not None
            and any(regex.fullmatch(__module__) for regex in IMPORTED_AS_MODULES)):
        for modobj, objname, modname in modmap.by_id[id(obj)]:
            if sys.modules[modname] is not main_module:
                return modname, objname
    return None, None

def _stash_modules(main_module):
    modmap = _module_map()
    newmod = ModuleType(main_module.__name__)

    imported = []
    imported_as = []
    imported_top_level = []  # keep separated for backward compatibility
    original = {}
    for name, obj in main_module.__dict__.items():
        if obj is main_module:
            original[name] = newmod  # self-reference
        elif obj is main_module.__dict__:
            original[name] = newmod.__dict__
        # Avoid incorrectly matching a singleton value in another package (ex.: __doc__).
        elif any(obj is singleton for singleton in (None, False, True)) \
                or isinstance(obj, ModuleType) and _is_builtin_module(obj):  # always saved by ref
            original[name] = obj
        else:
            source_module, objname = _lookup_module(modmap, name, obj, main_module)
            if source_module is not None:
                if objname == name:
                    imported.append((source_module, name))
                else:
                    imported_as.append((source_module, objname, name))
            else:
                try:
                    imported_top_level.append((modmap.top_level[id(obj)], name))
                except KeyError:
                    original[name] = obj

    if len(original) < len(main_module.__dict__):
        newmod.__dict__.update(original)
        newmod.__dill_imported = imported
        newmod.__dill_imported_as = imported_as
        newmod.__dill_imported_top_level = imported_top_level
        if getattr(newmod, '__loader__', None) is None and _is_imported_module(main_module):
            # Trick _is_imported_module() to force saving as an imported module.
            newmod.__loader__ = True  # will be discarded by save_module()
        return newmod
    else:
        return main_module

def _restore_modules(unpickler, main_module):
    try:
        for modname, name in main_module.__dict__.pop('__dill_imported'):
            main_module.__dict__[name] = unpickler.find_class(modname, name)
        for modname, objname, name in main_module.__dict__.pop('__dill_imported_as'):
            main_module.__dict__[name] = unpickler.find_class(modname, objname)
        for modname, name in main_module.__dict__.pop('__dill_imported_top_level'):
            main_module.__dict__[name] = __import__(modname)
    except KeyError:
        pass

#NOTE: 06/03/15 renamed main_module to main
def dump_module(
    filename: Union[str, os.PathLike] = None,
    module: Optional[Union[ModuleType, str]] = None,
    refimported: bool = False,
    **kwds
) -> None:
    for old_par, par in [('main', 'module'), ('byref', 'refimported')]:
        if old_par in kwds:
            message = "The argument %r has been renamed %r" % (old_par, par)
            if old_par == 'byref':
                message += " to distinguish it from dill.settings['byref']"
            warnings.warn(message + ".", PendingDeprecationWarning)
            if locals()[par]:  # the defaults are None and False
                raise TypeError("both %r and %r arguments were used" % (par, old_par))
    refimported = kwds.pop('byref', refimported)
    module = kwds.pop('main', module)

    from .settings import settings
    protocol = settings['protocol']
    main = module
    if main is None:
        main = _main_module
    elif isinstance(main, str):
        main = _import_module(main)
    if not isinstance(main, ModuleType):
        raise TypeError("%r is not a module" % main)
    if hasattr(filename, 'write'):
        file = filename
    else:
        if filename is None:
            filename = str(TEMPDIR/'session.pkl')
        file = open(filename, 'wb')
    try:
        pickler = Pickler(file, protocol, **kwds)
        pickler._original_main = main
        if refimported:
            main = _stash_modules(main)
        pickler._main = main     #FIXME: dill.settings are disabled
        pickler._byref = False   # disable pickling by name reference
        pickler._recurse = False # disable pickling recursion for globals
        pickler._session = True  # is best indicator of when pickling a session
        pickler._first_pass = True
        pickler._main_modified = main is not pickler._original_main
        pickler.dump(main)
    finally:
        if file is not filename:  # if newly opened file
            file.close()
    return

# Backward compatibility.
def dump_session(filename=None, main=None, byref=False, **kwds):
    warnings.warn("dump_session() has been renamed dump_module()", PendingDeprecationWarning)
    dump_module(filename, module=main, refimported=byref, **kwds)
dump_session.__doc__ = dump_module.__doc__

class _PeekableReader:
    """lightweight stream wrapper that implements peek()"""
    def __init__(self, stream):
        self.stream = stream
    def read(self, n):
        return self.stream.read(n)
    def readline(self):
        return self.stream.readline()
    def tell(self):
        return self.stream.tell()
    def close(self):
        return self.stream.close()
    def peek(self, n):
        stream = self.stream
        try:
            if hasattr(stream, 'flush'): stream.flush()
            position = stream.tell()
            stream.seek(position)  # assert seek() works before reading
            chunk = stream.read(n)
            stream.seek(position)
            return chunk
        except (AttributeError, OSError):
            raise NotImplementedError("stream is not peekable: %r", stream) from None

def _make_peekable(stream):
    """return stream as an object with a peek() method"""
    import io
    if hasattr(stream, 'peek'):
        return stream
    if not (hasattr(stream, 'tell') and hasattr(stream, 'seek')):
        try:
            return io.BufferedReader(stream)
        except Exception:
            pass
    return _PeekableReader(stream)

def _identify_module(file, main=None):
    """identify the name of the module stored in the given file-type object"""
    from pickletools import genops
    UNICODE = {'UNICODE', 'BINUNICODE', 'SHORT_BINUNICODE'}
    found_import = False
    try:
        for opcode, arg, pos in genops(file.peek(256)):
            if not found_import:
                if opcode.name in ('GLOBAL', 'SHORT_BINUNICODE') and \
                        arg.endswith('_import_module'):
                    found_import = True
            else:
                if opcode.name in UNICODE:
                    return arg
        else:
            raise UnpicklingError("reached STOP without finding main module")
    except (NotImplementedError, ValueError) as error:
        # ValueError occours when the end of the chunk is reached (without a STOP).
        if isinstance(error, NotImplementedError) and main is not None:
            # file is not peekable, but we have main.
            return None
        raise UnpicklingError("unable to identify main module") from error

def load_module(
    filename: Union[str, os.PathLike] = None,
    module: Optional[Union[ModuleType, str]] = None,
    **kwds
) -> Optional[ModuleType]:
    if 'main' in kwds:
        warnings.warn(
            "The argument 'main' has been renamed 'module'.",
            PendingDeprecationWarning
        )
        if module is not None:
            raise TypeError("both 'module' and 'main' arguments were used")
        module = kwds.pop('main')
    main = module
    if hasattr(filename, 'read'):
        file = filename
    else:
        if filename is None:
            filename = str(TEMPDIR/'session.pkl')
        file = open(filename, 'rb')
    try:
        file = _make_peekable(file)
        #FIXME: dill.settings are disabled
        unpickler = Unpickler(file, **kwds)
        unpickler._session = True

        # Resolve unpickler._main
        pickle_main = _identify_module(file, main)
        if main is None and pickle_main is not None:
            main = pickle_main
        if isinstance(main, str):
            if main.startswith('__runtime__.'):
                # Create runtime module to load the session into.
                main = ModuleType(main.partition('.')[-1])
            else:
                main = _import_module(main)
        if main is not None:
            if not isinstance(main, ModuleType):
                raise TypeError("%r is not a module" % main)
            unpickler._main = main
        else:
            main = unpickler._main

        # Check against the pickle's main.
        is_main_imported = _is_imported_module(main)
        if pickle_main is not None:
            is_runtime_mod = pickle_main.startswith('__runtime__.')
            if is_runtime_mod:
                pickle_main = pickle_main.partition('.')[-1]
            error_msg = "can't update{} module{} %r with the saved state of{} module{} %r"
            if is_runtime_mod and is_main_imported:
                raise ValueError(
                    error_msg.format(" imported", "", "", "-type object")
                    % (main.__name__, pickle_main)
                )
            if not is_runtime_mod and not is_main_imported:
                raise ValueError(
                    error_msg.format("", "-type object", " imported", "")
                    % (pickle_main, main.__name__)
                )
            if main.__name__ != pickle_main:
                raise ValueError(error_msg.format("", "", "", "") % (main.__name__, pickle_main))

        # This is for find_class() to be able to locate it.
        if not is_main_imported:
            runtime_main = '__runtime__.%s' % main.__name__
            sys.modules[runtime_main] = main

        loaded = unpickler.load()
    finally:
        if not hasattr(filename, 'read'):  # if newly opened file
            file.close()
        try:
            del sys.modules[runtime_main]
        except (KeyError, NameError):
            pass
    assert loaded is main
    _restore_modules(unpickler, main)
    if main is _main_module or main is module:
        return None
    else:
        return main

# Backward compatibility.
def load_session(filename=None, main=None, **kwds):
    warnings.warn("load_session() has been renamed load_module().", PendingDeprecationWarning)
    load_module(filename, module=main, **kwds)
load_session.__doc__ = load_module.__doc__

def load_module_asdict(
    filename: Union[str, os.PathLike] = None,
    update: bool = False,
    **kwds
) -> dict:
    if 'module' in kwds:
        raise TypeError("'module' is an invalid keyword argument for load_module_asdict()")
    if hasattr(filename, 'read'):
        file = filename
    else:
        if filename is None:
            filename = str(TEMPDIR/'session.pkl')
        file = open(filename, 'rb')
    try:
        file = _make_peekable(file)
        main_name = _identify_module(file)
        old_main = sys.modules.get(main_name)
        main = ModuleType(main_name)
        if update:
            if old_main is None:
                old_main = _import_module(main_name)
            main.__dict__.update(old_main.__dict__)
        else:
            main.__builtins__ = __builtin__
        sys.modules[main_name] = main
        load_module(file, **kwds)
    finally:
        if not hasattr(filename, 'read'):  # if newly opened file
            file.close()
        try:
            if old_main is None:
                del sys.modules[main_name]
            else:
                sys.modules[main_name] = old_main
        except NameError:  # failed before setting old_main
            pass
    main.__session__ = str(filename)
    return main.__dict__


# Internal exports for backward compatibility with dill v0.3.5.1
# Can't be placed in dill._dill because of circular import problems.
for name in (
    '_lookup_module', '_module_map', '_restore_modules', '_stash_modules',
    'dump_session', 'load_session' # backward compatibility functions
):
    setattr(_dill, name, globals()[name])
del name
