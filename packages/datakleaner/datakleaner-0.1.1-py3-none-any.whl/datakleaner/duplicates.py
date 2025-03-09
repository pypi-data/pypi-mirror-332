# Import the necessary libraries
import pandas as pd


# Create the 'DuplicateHandler' class
class DuplicateHandler:
    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def remove_duplicates(self, keep="first"):
        """
        Removes duplicate rows from the dataset.

        Parameters:
        keep (str): "first" (default) keeps the first occurrence, "last" keeps the last, "none" removes all.

        Returns:
        pd.DataFrame: DataFrame with duplicates removed.
        """
        if keep not in ["first", "last", "none"]:
            raise ValueError("Invalid option for 'keep'. Choose from 'first', 'last', or 'none'.")

        if keep == "none":
            self.df = self.df[self.df.duplicated(keep=False) == False]
            print("All duplicate rows removed.")

        else:
            count = self.df.duplicated().sum()
            self.df = self.df.drop_duplicates(keep=keep)
            print(f"{count} duplicate rows removed.")

        print(f"Duplicate rows removed using keep: '{keep}'")

        return self.df


# Example use case
if __name__ == '__main__':
    data = {
        'A': [1, 2, 2, 3, 4, 4, 4, 5],
        'B': ['x', 'y', 'y', 'z', 'w', 'w', 'w', 'v']
    }

    df = pd.DataFrame(data)

    handler = DuplicateHandler(df)
    cleaned_df = handler.remove_duplicates(keep='first')
    print(cleaned_df)

