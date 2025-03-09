# Import necessary libraries
import pandas as pd
import numpy as np
from scipy import stats


# Create 'Diagnoser' class
class Diagnoser:
    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()
        self.missing_values = {}
        self.duplicate_count = 0
        self.outliers = {}

    def check_missing_values(self):
        """Checks for missing values in each column."""
        missing = self.df.isnull().sum()
        self.missing_values = missing[missing > 0].to_dict()
        return self.missing_values

    def check_duplicates(self):
        """Count the number of duplicate rows."""
        self.duplicate_count = self.df.duplicated().sum()
        return self.duplicate_count

    def check_outliers(self, method='iqr', threshold=3):
        """
        Identifies outliers using IQR or z-score method.
        IQR method is used by default.

        Parameters:
        method (str): "iqr" (Inter-quarter range) or "zscore".
        threshold (float): Threshold for Z-score (default is 3).

        Returns:
        dict: Dictionary with column names and outlier indices.
        """

        num_cols = self.df.select_dtypes(include=[np.number]).columns
        self.outliers = {}

        for col in num_cols:
            if method == "iqr":
                Q1 = self.df[col].quantile(0.25)
                Q3 = self.df[col].quantile(0.75)
                iqr = Q3 - Q1
                lower_bound = Q1 - 1.5 * iqr
                upper_bound = Q3 + 1.5 * iqr
                outlier_indices = self.df[(self.df[col] < lower_bound) | (self.df[col] > upper_bound)].index.tolist()

            elif method == "zscore":
                z_score = np.abs(stats.zscore(self.df[col], nan_policy='omit'))
                outlier_indices = self.df[z_score > threshold].index.tolist()

            else:
                raise ValueError("Invalid method. Choose 'iqr' or 'zscore'.")

            if outlier_indices:
                self.outliers[col] = outlier_indices

        return self.outliers

    def generate_report(self):
        """Generates a summary report of missing values, duplicates, and outliers."""

        self.check_missing_values()
        self.check_duplicates()
        self.check_outliers()

        print("--- Data Diagnosis Report ---")
        print(
            f"Missing Values: {self.missing_values if self.missing_values else 'No missing values found in the dataset'}")
        print(f"Duplicate Rows: {self.duplicate_count}")
        print(f"Outliers Found: {self.outliers if self.outliers else 'No outliers found in the dataset.'}")


# Example Usage
if __name__ == "__main__":
    data = {
        'A': [1, 2, 3, 4, 5, 4],  # Outlier at 100, Missing value
        'B': [10, 12, 14, 16, 18, 200],  # Outlier at 200
        'C': [5, 7, 9, 11, 13, 15],
        'D': ['x', 'y', 'y', 'z', 'w', 'w']
    }
    df = pd.DataFrame(data)

    diagnoser = Diagnoser(df)
    diagnoser.generate_report()

