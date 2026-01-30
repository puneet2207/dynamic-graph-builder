# converts raw data sources into Pandas Dataframe

from typing import List, Dict, Any
import pandas as pd

def load_from_csv(file_path: str) -> pd.DataFrame:
    """
    Load a dataset from a csv file into a pandas dataframe.
    """
    try: 
        df= pd.read_csv(file_path)
    except Exception as exc:
        raise RuntimeError(f"Failed to load CSV file: {file_path}") from exc
    
    if df.empty:
        raise ValueError("Loaded CSV file is empty")
    
    return df

def load_from_records(records: List[str, Any]) -> pd.DataFrame:
    """
    Load a dataset from a list of dictionaries (API-style data).
    """
    if not records:
        raise ValueError("Input records list is empty")

    try:
        df = pd.DataFrame(records)
    except Exception as exc:
        raise RuntimeError("Failed to convert records to Dataframe") from exc
    
    if df.empty:
        raise ValueError("Generated dataframe is empty")
    
    return df