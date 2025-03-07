from pyspark.sql import DataFrame
from pyspark.sql import functions as F
from pyspark.sql.types import (
    DataType,
    NullType,
    BooleanType,
    IntegerType,
    LongType,
    FloatType,
    DoubleType,
    DecimalType,
    DateType,
    TimestampType,
    StringType,
)
import uuid, enum
from .datasampleloader import DataSampleLoaderLib
from .httpclient import ProphecyRequestsLib


class DiffKeys(enum.Enum):
    JOINED = "joined"
    SUMMARY = "summary"
    CLEANED = "cleaned"
    EXPECTED = "expected"
    GENERATED = "generated"
    KEY_COLUMNS = "keyCols"
    VALUE_COLUMNS = "valueCols"


class DataFrameDiff:
    COMPUTED_DIFFS = {}

    @classmethod
    def get_precedence(cls, dt: DataType) -> int:
        """
        Assign a numeric precedence/rank to Spark data types.
        Lower value = narrower type, Higher value = broader type.
        """
        if isinstance(dt, NullType):
            # Null can be promoted to anything else
            return 0
        elif isinstance(dt, BooleanType):
            return 1
        elif isinstance(dt, IntegerType):
            return 2
        elif isinstance(dt, LongType):
            return 3
        elif isinstance(dt, FloatType):
            return 4
        elif isinstance(dt, DoubleType):
            return 5
        elif isinstance(dt, DecimalType):
            # Treat decimal as broader than basic floats/doubles for numeric contexts
            return 6
        elif isinstance(dt, DateType):
            return 7
        elif isinstance(dt, TimestampType):
            return 8
        elif isinstance(dt, StringType):
            return 9
        # Fallback for complex or unhandled types
        return 99

    @classmethod
    def find_common_type(cls, dt1: DataType, dt2: DataType) -> DataType:
        """
        Find a 'common' Spark data type for dt1 and dt2 based on simplified precedence rules.
        """
        # If they're exactly the same (including decimal precision/scale), just return dt1
        if dt1 == dt2:
            return dt1

        # Both are DecimalType but differ in precision or scale
        if isinstance(dt1, DecimalType) and isinstance(dt2, DecimalType):
            # Pick the "wider" decimal
            precision = max(dt1.precision, dt2.precision)
            scale = max(dt1.scale, dt2.scale)
            return DecimalType(precision=precision, scale=scale)

        # If either is NullType, pick the other
        if isinstance(dt1, NullType):
            return dt2
        if isinstance(dt2, NullType):
            return dt1

        # Otherwise, compare precedence
        prec1 = cls.get_precedence(dt1)
        prec2 = cls.get_precedence(dt2)

        # If both are numeric (including decimals), pick the broader
        numeric_types = (
            BooleanType,
            IntegerType,
            LongType,
            FloatType,
            DoubleType,
            DecimalType,
        )
        if isinstance(dt1, numeric_types) and isinstance(dt2, numeric_types):
            return dt1 if prec1 >= prec2 else dt2

        # Date <-> Timestamp => Timestamp
        if (isinstance(dt1, DateType) and isinstance(dt2, TimestampType)) or (
            isinstance(dt2, DateType) and isinstance(dt1, TimestampType)
        ):
            return TimestampType()

        # In all other cases (e.g. one is StringType, or higher precedence):
        # todo recursive handling for array and struct types.
        return dt1 if prec1 > prec2 else dt2

    @classmethod
    def align_dataframes_schemas(
        cls, df1: DataFrame, df2: DataFrame
    ) -> (DataFrame, DataFrame):
        """
        Aligns df1 and df2 so that columns with the same name have the same data type.
        Returns two new DataFrames (df1_aligned, df2_aligned).
        """
        df1_aligned = df1
        df2_aligned = df2

        # Columns that exist in both DataFrames
        common_cols = set(df1.columns).intersection(set(df2.columns))

        for col_name in common_cols:
            dt1 = df1.schema[col_name].dataType
            dt2 = df2.schema[col_name].dataType

            # Determine the common type
            common_dt = cls.find_common_type(dt1, dt2)

            # Important: Compare the entire DataType object, not just the class.
            if dt1 != common_dt:
                df1_aligned = df1_aligned.withColumn(
                    col_name, F.col(col_name).cast(common_dt)
                )
            if dt2 != common_dt:
                df2_aligned = df2_aligned.withColumn(
                    col_name, F.col(col_name).cast(common_dt)
                )

        return df1_aligned, df2_aligned

    @classmethod
    def split_df_by_pk_uniqueness(cls, df, key_columns):
        """
        Returns two DataFrames:
          1) df_unique: Rows where 'key_columns' is unique (exactly 1 occurrence)
          2) df_not_unique: Rows where 'key_columns' occur more than once
        """
        # Create a unique column name for counting that does not collide with existing columns
        count_alias = f"__count_{uuid.uuid4().hex}"

        # 1) Group by the key columns and count (using the alias)
        pk_counts = df.groupBy(key_columns).agg(F.count("*").alias(count_alias))

        # 2) Separate the PKs that appear once vs. more than once, and drop the aggregator column
        pk_once = pk_counts.filter(F.col(count_alias) == 1).select(
            *key_columns
        )  # Only select key columns to avoid carrying the count_alias
        pk_not_once = pk_counts.filter(F.col(count_alias) > 1).select(
            *key_columns
        )  # Only select key columns

        # 3) Join with the original df to get rows
        df_unique = df.join(pk_once, on=key_columns, how="inner")
        df_not_unique = df.join(pk_not_once, on=key_columns, how="inner")

        return df_unique, df_not_unique

    @classmethod
    def create_joined_df(cls, df1, df2, key_columns, value_columns):
        """
        Compare two DataFrames and identify presence in left, right, and differences in values.

        :param df1: First / Calculated DataFrame (left)
        :param df2: Second / Expected DataFrame (right)
        :param key_columns: List of key columns for joining
        :param value_columns: List of value columns to compare
        :return: Resultant DataFrame with key columns, presence flags, and value comparison
        """

        df1, df2 = cls.align_dataframes_schemas(df1, df2)

        # Perform a full outer join on the key columns
        joined_df = df1.alias("left").join(
            df2.alias("right"), on=key_columns, how="full_outer"
        )

        # Compute coalesced key columns and presence flags
        coalesced_keys = [
            F.coalesce(F.col(f"left.{col}"), F.col(f"right.{col}")).alias(col)
            for col in key_columns
        ]

        presence_in_left = (
            F.when(
                F.expr(
                    " AND ".join(
                        [
                            f"coalesce(left.{col}, right.{col}) = left.{col}"
                            for col in key_columns
                        ]
                    )
                ),
                1,
            )
            .otherwise(0)
            .alias("presence_in_left")
        )

        presence_in_right = (
            F.when(
                F.expr(
                    " AND ".join(
                        [
                            f"coalesce(left.{col}, right.{col}) = right.{col}"
                            for col in key_columns
                        ]
                    )
                ),
                1,
            )
            .otherwise(0)
            .alias("presence_in_right")
        )

        # Build the left and right structs for the value columns.
        # If a column is missing in a DataFrame, we substitute it with a null literal.
        left_value_exprs = [
            (
                F.col(f"left.{col}").alias(col)
                if col in df1.columns
                else F.lit(None).alias(col)
            )
            for col in value_columns
        ]
        right_value_exprs = [
            (
                F.col(f"right.{col}").alias(col)
                if col in df2.columns
                else F.lit(None).alias(col)
            )
            for col in value_columns
        ]

        left_struct = F.struct(*left_value_exprs).alias("left_values")
        right_struct = F.struct(*right_value_exprs).alias("right_values")

        # Select the final result
        result_df = joined_df.select(
            *coalesced_keys,  # Coalesced key columns
            presence_in_left,  # Presence flag for left
            presence_in_right,  # Presence flag for right
            left_struct,  # Struct containing left values (with missing columns as null)
            right_struct,  # Struct containing right values
        )

        return result_df

    @classmethod
    def add_row_matches_column(cls, joined_df):
        """
        Adds a new column 'row_matches' to the DataFrame that indicates whether
        the values in 'left_values' and 'right_values' columns are equal.
        """

        left_struct = "left_values"
        right_struct = "right_values"
        return joined_df.withColumn(
            "row_matches", F.expr(f"{left_struct} = {right_struct}")
        )

    @classmethod
    def add_column_comparison_results(cls, joined_df):
        """
        Adds a new column to the DataFrame containing comparison results between two struct columns.

        This function compares corresponding fields within two specified struct columns (`left_struct` and `right_struct`)
        and aggregates the comparison results into a new struct column (`comparison_struct`). Each field in the new struct
        indicates whether the corresponding fields in the input structs are equal.
        """
        left_struct = "left_values"
        right_struct = "right_values"
        comparison_struct = "compared_values"

        # Retrieve the list of fields from the left struct column
        left_fields = joined_df.select(f"{left_struct}.*").columns

        # Generate comparison expressions for each field in the struct
        comparison_expressions = [
            (F.col(f"{left_struct}.{field}") == F.col(f"{right_struct}.{field}")).alias(
                field
            )
            for field in left_fields
        ]

        # Combine individual comparison results into a single struct column
        comparison_struct_col = F.struct(*comparison_expressions)

        # Add the comparison struct column to the DataFrame
        return joined_df.withColumn(comparison_struct, comparison_struct_col)

    @classmethod
    def compute_mismatch_summary(cls, joined_df):
        """
        Computes summary statistics for mismatches across specified columns in the joined DataFrame.

        This function calculates:
        - The number of rows where all specified columns match.
        - The number of rows with at least one mismatch.
        - The total number of mismatches across all specified columns and rows.
        - The count of matches and mismatches for each individual specified column.

        Args:
            joined_df (DataFrame): The input Spark DataFrame containing a `compared_values` struct column
                                   with boolean fields indicating match status for each specified column,
                                   and a `row_matches` boolean column indicating if the entire row matches.

        Returns:
            DataFrame: A summary DataFrame with the following columns:
                - rows_matching (Long): Number of rows where all specified columns match.
                - rows_not_matching (Long): Number of rows with at least one mismatch.
                - <column>_match_count (Long): Number of matches for each specified column.
                - <column>_mismatch_count (Long): Number of mismatches for each specified column.
        """

        comparison_struct = "compared_values"

        fields = joined_df.select(f"{comparison_struct}.*").columns

        # Build aggregators for match and mismatch counts for each specified column
        per_column_aggregators = []
        for column in fields:
            # Aggregator for the number of matches in the current column
            match_aggregator = F.sum(
                F.when(F.col(f"{comparison_struct}.{column}"), 1).otherwise(0)
            ).alias(f"{column}_match_count")
            per_column_aggregators.append(match_aggregator)

            # Aggregator for the number of mismatches in the current column
            mismatch_aggregator = F.sum(
                F.when(~F.col(f"{comparison_struct}.{column}"), 1).otherwise(0)
            ).alias(f"{column}_mismatch_count")
            per_column_aggregators.append(mismatch_aggregator)

        # New aggregators for key column matching.
        # A key is considered matching if both presence_in_left and presence_in_right are 1.
        key_cols_match_expr = F.sum(
            F.when(
                (F.col("presence_in_left") == 1) & (F.col("presence_in_right") == 1), 1
            ).otherwise(0)
        ).alias("key_columns_match_count")

        key_cols_mismatch_expr = F.sum(
            F.when(
                ~((F.col("presence_in_left") == 1) & (F.col("presence_in_right") == 1)),
                1,
            ).otherwise(0)
        ).alias("key_columns_mismatch_count")

        # Aggregate all summary statistics into a single DataFrame.
        summary_df = joined_df.agg(
            # Count of rows where all specified columns match
            F.sum(F.when(F.col("row_matches"), 1).otherwise(0)).alias("rows_matching"),
            # Count of rows with at least one mismatch
            F.sum(F.when(~F.col("row_matches"), 1).otherwise(0)).alias(
                "rows_not_matching"
            ),
            # Count of key column matches and mismatches
            key_cols_match_expr,
            key_cols_mismatch_expr,
            # Include all per-column match and mismatch aggregators
            *per_column_aggregators,
        )

        return summary_df

    @classmethod
    def get_value_columns(cls, df1, df2, key_columns):
        _all_columns = set(df1.columns).union(set(df2.columns))
        return list(_all_columns - set(key_columns))

    @classmethod
    def get_columns_schema(cls, df):
        return [
            {"name": field.name, "type": field.dataType.simpleString()}
            for field in df.schema.fields
        ]

    @classmethod
    def get_diff_summary_dict(cls, diff_key):
        diff_entry = cls.COMPUTED_DIFFS[diff_key]
        summary_df, value_columns = (
            diff_entry[DiffKeys.SUMMARY.value],
            diff_entry[DiffKeys.VALUE_COLUMNS.value],
        )
        key_columns = diff_entry[DiffKeys.KEY_COLUMNS.value]
        expected_df = diff_entry[DiffKeys.EXPECTED.value]
        generated_df = diff_entry[DiffKeys.GENERATED.value]

        summary_row = summary_df.collect()[0].asDict()
        rows_matching = summary_row["rows_matching"]
        rows_not_matching = summary_row["rows_not_matching"]
        total_rows = rows_matching + rows_not_matching

        # Calculate column match statistics
        perfect_column_matches = 0
        for col in value_columns:
            if summary_row[f"{col}_match_count"] == total_rows:
                perfect_column_matches += 1

        # Calculate dataset matching status
        dataset_match_status = "Matching" if rows_not_matching == 0 else "Not Matching"
        match_percentage = (
            round((rows_matching / total_rows * 100)) if total_rows > 0 else 0
        )

        # Helper function to get dataset stats
        def get_dataset_stats(df, key_cols):
            unique_df, duplicate_df = cls.split_df_by_pk_uniqueness(df, key_cols)
            return {
                "columns": cls.get_columns_schema(df),
                "rowsCount": df.count(),
                "uniquePkCount": unique_df.count(),
                "duplicatePkCount": duplicate_df.count(),
            }

        return {
            "label": diff_key,
            "data": {
                "summaryTiles": [
                    {
                        "title": "Datasets matching status",
                        "text": dataset_match_status,
                        "badgeContent": f"{match_percentage}",
                        "isPositive": rows_not_matching == 0,
                        "order": 0,
                        "orderType": "MatchingStatus",
                        "toolTip": "The percentage of rows that match between the expected and generated datasets.",
                    },
                    {
                        "title": "Number of columns matching",
                        "text": f"{perfect_column_matches + len(key_columns)}/{len(value_columns) + len(key_columns)}",
                        "badgeContent": f"{round(((perfect_column_matches + len(key_columns))/(len(value_columns) + len(key_columns)))*100)}",
                        "isPositive": perfect_column_matches == len(value_columns),
                        "order": 1,
                        "orderType": "ColumnMatch",
                        "toolTip": "The percentage of columns that match between the expected and generated datasets.",
                    },
                    {
                        "title": "Number of rows matching",
                        "text": f"{rows_matching:,}/{total_rows:,}",
                        "badgeContent": f"{match_percentage}",
                        "isPositive": rows_matching == total_rows,
                        "order": 2,
                        "orderType": "RowMatch",
                        "toolTip": "The percentage of rows that match between the expected and generated datasets.",
                    },
                ],
                "expData": get_dataset_stats(expected_df, key_columns),
                "genData": get_dataset_stats(generated_df, key_columns),
                "commonData": {
                    "keyColumns": key_columns,
                    "columnComparisons": {
                        col: {
                            "matches": summary_row[f"{col}_match_count"],
                            "mismatches": summary_row[f"{col}_mismatch_count"],
                        }
                        for col in set(expected_df.columns)
                        .intersection(set(generated_df.columns))
                        .intersection(set(value_columns))
                    },
                    "rowsMatchingCount": rows_matching,
                    "rowsMismatchingCount": rows_not_matching,
                    "keyColumnsMatchCount": summary_row["key_columns_match_count"],
                    "keyColumnsMismatchCount": summary_row[
                        "key_columns_mismatch_count"
                    ],
                },
            },
        }

    @classmethod
    def clean_joined_df(cls, joined_df, key_columns, value_columns, left_df, right_df):
        """
        Transforms the joined DataFrame into a cleaned DataFrame with the following structure:

        - For each key column: selects the value from the coalesced key column.
        - For each value column (from the union of left and right values):
            • If the compared field (from 'compared_values') is True (i.e. the left and right values match),
              then include an array with a single element (the common value).
            • If not and the column exists in both DataFrames, include an array with both values [left_value, right_value].
            • If the column exists only in one DataFrame, then include an array with the available value only.
        - Also preserves the 'row_matches', 'presence_in_left', and 'presence_in_right' columns.

        Example output schema for a given row:
        ┌───────────┬───────────┬──────────────────┬─────────────────┬─────────────────────┬─────────────────────┬─────────────────────┐
        │ FirstName │ LastName  │      Class       │     Region      │   row_matches       │  presence_in_left   │  presence_in_right  │
        │           │           │  (array<double>) │ (array<string>) │   (boolean)         │   (boolean)         │   (boolean)         │
        │           │           │      ...         │     ...         │                     │                     │                     │
        └───────────┴───────────┴──────────────────┴─────────────────┴─────────────────────┴─────────────────────┴─────────────────────┘
        (Each value column becomes an array of either one or two elements.)
        """
        select_exprs = []

        # Add key columns directly.
        for col_name in key_columns:
            select_exprs.append(F.col(col_name))

        # For each value column, decide whether to create an array
        # with one value (if only exists in one DataFrame, or if left and right match)
        # or two values (if they differ and exist in both DataFrames).
        for col_name in value_columns:
            if col_name in left_df.columns and col_name in right_df.columns:
                select_exprs.append(
                    F.when(
                        F.col(f"compared_values.{col_name}") == True,
                        F.array(F.col(f"left_values.{col_name}")),
                    )
                    .otherwise(
                        F.array(
                            F.col(f"left_values.{col_name}"),
                            F.col(f"right_values.{col_name}"),
                        )
                    )
                    .alias(col_name)
                )
            elif col_name in left_df.columns:
                select_exprs.append(
                    F.array(F.col(f"left_values.{col_name}")).alias(col_name)
                )
            elif col_name in right_df.columns:
                select_exprs.append(
                    F.array(F.col(f"right_values.{col_name}")).alias(col_name)
                )

        # Append the additional columns.
        select_exprs.append(F.col("row_matches"))
        select_exprs.append(F.col("presence_in_left"))
        select_exprs.append(F.col("presence_in_right"))

        return joined_df.select(*select_exprs)

    @classmethod
    def create_diff(cls, expected_df, generated_df, key_columns, diff_key):
        value_columns = cls.get_value_columns(expected_df, generated_df, key_columns)
        joined_df = cls.create_joined_df(
            # pass unique df
            df1=cls.split_df_by_pk_uniqueness(generated_df, key_columns=key_columns)[0],
            df2=cls.split_df_by_pk_uniqueness(expected_df, key_columns=key_columns)[0],
            key_columns=key_columns,
            value_columns=value_columns,
        )
        joined_df = cls.add_row_matches_column(joined_df)
        joined_df = cls.add_column_comparison_results(joined_df)
        summary_df = cls.compute_mismatch_summary(joined_df)
        clean_joined_df = cls.clean_joined_df(
            joined_df,
            key_columns,
            value_columns,
            left_df=generated_df,
            right_df=expected_df,
        )

        cls.COMPUTED_DIFFS[diff_key] = {
            DiffKeys.JOINED.value: joined_df,
            DiffKeys.SUMMARY.value: summary_df,
            DiffKeys.CLEANED.value: clean_joined_df,
            DiffKeys.EXPECTED.value: expected_df,
            DiffKeys.GENERATED.value: generated_df,
            DiffKeys.KEY_COLUMNS.value: key_columns,
            DiffKeys.VALUE_COLUMNS.value: value_columns,
        }

    @classmethod
    def datasampleloader_register(cls, diff_key: str, _type: DiffKeys) -> str:
        diff_entry = cls.COMPUTED_DIFFS[diff_key]
        df = diff_entry[_type.value]
        dsl_key = str(uuid.uuid4())
        DataSampleLoaderLib.register(key=dsl_key, df=df, create_truncated_columns=False)
        return dsl_key
