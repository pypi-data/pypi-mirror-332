# Import the necessary libraries
import pandas as pd
import numpy as np


# Create the 'MissingDataHandler' class
class MissingDataHandler:
    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def handle_missing_values(self, column, method="drop", custom_value=None):
        """
        Handles missing values based on user-defined method.

        Parameters:
        column (str): The name of the column to be cleaned as string.
        method (str): "drop", "mean", "median", "mode", "custom".
        custom_value (number): The value to fill missing data.

        Returns: pd.DataFrame: DataFrame with missing values handled.
        """

        if method == "drop":
            self.df = self.df.dropna(subset=[column])

        elif method == "mean":
            self.df[column] = self.df[column].fillna(self.df[column].mean())

        elif method == "median":
            self.df[column] = self.df[column].fillna(self.df[column].median())

        elif method == "mode":
            self.df[column] = self.df[column].fillna(self.df[column].mode().iloc[0])

        elif method == "custom":
            self.df[column] = self.df[column].fillna(custom_value)

        else:
            raise ValueError("Invalid method. Choose from 'drop', 'mean', 'median', 'mode', or 'custom'.")

        print(f"\n Missing values handled using method: '{method}'")
        return self.df


# # Example Usage
if __name__ == "__main__":
    data = {
        'A': [1, 2, np.nan, 4, 5],
        'B': [np.nan, 1, 2, 3, np.nan],
        'C': [10, 20, 30, 40, 50]
    }
    df = pd.DataFrame(data)

    handler = MissingDataHandler(df)
    cleaned_df = handler.handle_missing_values(['A', 'B'], method="mean")
    print(cleaned_df)

