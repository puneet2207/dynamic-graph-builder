from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field

class ColumnType(str, Enum):
    numerical = "numerical"
    categorical = "categorical"
    datetime = "datetime"

class ChartType(str, Enum):
    line = "line"
    bar = "bar"
    pie ="pie"
    scatter = "scatter"
    scatter_3d = "scatter_3d"
    histogram ="histogram"
    box ="box"
    heatmap = "heatmap"

#Dataset schema models.

class ColumnSchema(BaseModel):
    """
    Describes a single column in the dataset.
    """
    name: str = Field(..., description= "Column name")
    dtype: ColumnType = Field(..., description="Detected column type")
    unique_values: Optional[int] = Field(None, description="Number of unique values")

class DataSchema(BaseModel):
    """
    Describes the overall dataset structure.
    """
    columns: List[ColumnSchema]
    row_count: int

# chart specification model

class ChartSpec(BaseModel):
    """
    This is the strict contact that the LLM must follow.
    The LLM is only allowed to return data matching this schema.
    """
    chart_type: ChartType

    x: Optional[str] = Field(
        None, description = "column name for x-axis"
    )
    y: Optional[str] = Field(
        None, description = "column name for y-axis"
    )
    z: Optional[str] = Field(
        None, description = "column name for z-axis (for 3D charts only.)"
    )

    title: Optional[str] = Field(
        None, description = "Chart Title"
    )
    x_type: Optional[ColumnType] = Field(
        None, description = "Data type for x-axis"
    )
    y_type: Optional[ColumnType] = Field(
        None, description = "Data type for y-axis"
    )
    z_type: Optional[ColumnType] = Field(
        None, description = "Data type for z-axis"
    )