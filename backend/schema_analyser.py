# This module will inspects each column and determines the column name,
# semantic type, number of unique values and returns a Dataset schema object.

import pandas as pd
from backend.models import ColumnSchema, ColumnType, DataSchema

def detect_column_type(series: pd.Series) -> ColumnType:
    """
    Detect the semantic type of a pandas series.
    """
    # datetime detection
    if pd.api.types.is_datetime64_any_dtype(series):
        return ColumnType.datetime
    
    # coercing to datetime (safe check)
    try:
        parsed = pd.to_datetime(series, errors= "raise")
        if not parsed.isna().any():
            return ColumnType.datetime
    except Exception:
        pass

    # Numerical detection
    if pd.api.types.is_numeric_dtype(series):
        return ColumnType.numerical
    
    # categorical
    return ColumnType.categorical

def analyze_schema(df: pd.Dataframe) -> DataSchema:
    """
    Analyse a dataframe and return its DataSchema.
    """
    columns = []

    for col_name in df.columns:
        series = df[col_name]

        column_type = detect_column_type(series)

        unique_values = None
        try:
            unique_values = series.nunique(dropna=True)
        except Exception:
            pass

        columns.append(
            ColumnSchema(
                name=col_name,
                dtype=column_type,
                unique_values= unique_values
            )
        )
    
    return DataSchema(
        columns=columns,
        row_count=len(df)
    )
