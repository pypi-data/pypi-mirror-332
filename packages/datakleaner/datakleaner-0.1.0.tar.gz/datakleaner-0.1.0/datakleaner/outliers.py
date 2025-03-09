# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class OutlierHandler:
    def __init__(self, df: pd.DataFrame):
        """Initialize the OutlierHandler with a copy of the DataFrame."""
        self.df = df.copy()

    def visualise_outliers(self, columns=None):
        """Displays box plots for detecting outliers visually."""
        if columns is None:
            columns = self.df.select_dtypes(include=[np.number]).columns

        plt.figure(figsize=(12, 6))
        self.df[columns].boxplot()
        plt.title("Boxplot for Outlier Detection")
        plt.xticks(rotation=45)
        plt.show()

    def handle_outliers(self, strategy="remove", method="median",
                        check_type="iqr", threshold=3):
        """
        Detects and handles outliers by either removing or imputing them.

        Parameters:
        strategy (str): "remove" (drop outliers) or "impute" (replace outliers).
        method (str): "mean", "median", or "mode" for imputation.
        check_type (str): "iqr" (Inter-quartile Range) or "zscore" (Z-score).
        threshold (float): Threshold for Z-score (default is 3).

        Returns:
        pd.DataFrame: DataFrame with outliers handled.
        """
        outliers = {}
        num_cols = self.df.select_dtypes(include=[np.number]).columns

        for col in num_cols:
            if check_type == "iqr":
                Q1 = self.df[col].quantile(0.25)
                Q3 = self.df[col].quantile(0.75)
                IQR = Q3 - Q1
                lower_bound = Q1 - 1.5 * IQR
                upper_bound = Q3 + 1.5 * IQR
                outlier_indices = self.df.index[(self.df[col] < lower_bound) | (self.df[col] > upper_bound)].tolist()

            elif check_type == "zscore":
                mean = self.df[col].mean()
                std = self.df[col].std()
                outlier_indices = self.df.index[(np.abs((self.df[col] - mean) / std) > threshold)].tolist()

            else:
                raise ValueError("Invalid check_type. Choose 'iqr' or 'zscore'.")

            if outlier_indices:
                outliers[col] = outlier_indices

        if not outliers:
            print("No outliers detected.")
            return self.df  # Return unchanged DataFrame if no outliers exist

        print("Outlier Summary:")
        for col, indices in outliers.items():
            print(f"Column: {col}, Outliers at indices: {indices}")

        # Ensure all outliers are handled before modifying the DataFrame
        all_outlier_indices = sorted(
            set(idx for indices in outliers.values() for idx in indices), reverse=True)

        if strategy == "remove":
            self.df = self.df.drop(index=all_outlier_indices).reset_index(drop=True)

            print(f"Outliers handled using strategy: '{strategy}'")

        elif strategy == "impute":
            for col, indices in outliers.items():
                if method == "mean":
                    replacement = self.df[col].mean()

                elif method == "median":
                    replacement = self.df[col].median()

                elif method == "mode":
                    replacement = self.df[col].mode().iloc[0]

                else:
                    raise ValueError("Invalid method. Choose 'mean', 'median', or 'mode'.")

                self.df.loc[indices, col] = replacement

            print(f"Outliers handled using strategy: '{strategy}', method: '{method}', check_type: '{check_type}'")
        else:
            raise ValueError("Invalid strategy. Choose 'remove' or 'impute'.")

        return self.df


# Example Usage
if __name__ == "__main__":
    data = {
        "A": [1, 2, 3, 6, 5, 100],  # Outlier at index 5
        "B": [10, 12, 14, 16, 18, 200],  # Outlier at index 5
        "C": [5, 7, 9, 11, 13, 15],
    }
    df = pd.DataFrame(data)

    handler = OutlierHandler(df)
    cleaned_df = handler.handle_outliers(strategy="impute", check_type="zscore", threshold=2)
    print(cleaned_df)
