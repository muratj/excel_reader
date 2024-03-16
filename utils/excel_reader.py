from pathlib import Path
from typing import Optional

import pandas as pd
import numpy as np


def get_excel_data(file_name: str | Path, row: str | int, column: str | int) -> Optional[str]:
    """
    Retrieve data from an Excel file based on row and column names or numbers.

    Parameters:
    - file_name (str): The name of the Excel file.
    - row (str/int): The name or number of the row. 
    When provided a string, it refers to the first column (A) values.
    - column (str/int): The name or number of the column.

    Returns:
    - The data at the specified row and column.
    """
    try:
        data = ''
        # Read the Excel file into a Pandas DataFrame
        df = pd.read_excel(file_name)

        if isinstance(row, int) and isinstance(column, int):
            # iloc to locate the specific cell based on row and column numbers
            data = df.iloc[row, column]
        elif isinstance(row, int) and isinstance(column, str):
            column_number = np.where(df.columns.values == column)[0][0]
            data = df.iloc[row, column_number]
        elif isinstance(row, str) and isinstance(column, str):
            # loc to locate the specific cell based on row and column names
            row_identifier = df.columns.values[0]
            data = df.loc[df[row_identifier] == row, column].values[0]
        elif isinstance(row, str) and isinstance(column, int):
            column_name = df.columns.values[column]
            row_identifier = df.columns.values[0]
            data = df.loc[df[row_identifier] == row, column_name].values[0]

        return data
    except Exception as e:
        print(f"Error: {e}")
        return None
