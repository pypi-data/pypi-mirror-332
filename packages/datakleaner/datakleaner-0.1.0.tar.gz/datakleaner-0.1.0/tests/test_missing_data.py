# Import necessary libraries
import pytest
import pandas as pd
import numpy as np
from datakleaner.missing_data import MissingDataHandler


@pytest.fixture
def sample_dataframe():
    data = {
        'A': [1, 2, np.nan, 4, 5, np.nan],  # Two missing values
        'B': [10, np.nan, 14, 16, np.nan, 20],  # Two missing values
        'C': ['x', 'y', 'z', np.nan, 'w', 't'],  # One missing value
    }
    return pd.DataFrame(data)


@pytest.fixture
def handler_instance(sample_dataframe):
    return MissingDataHandler(sample_dataframe)


def test_handle_missing_drop(handler_instance):
    handler_instance.handle_missing_values("A", method="drop")
    assert handler_instance.df["A"].isnull().sum() == 0  # No missing values should remain in 'A'.


def test_handle_missing_mean():
    df = pd.DataFrame({
        'A': [1, 2, np.nan, 4, 5],
        'B': [10, np.nan, 14, 16, 18]
    })

    handler = MissingDataHandler(df)
    df = handler.handle_missing_values('B', method="mean")
    assert df["B"].isnull().sum() == 0  # No missing value in 'B'
    assert df.loc[1, "B"] == df["B"].mean()  # Check if missing value was replaced with mean


def test_handle_missing_median():
    df = pd.DataFrame({
        'A': [1, 2, np.nan, 4, 5],
        'B': [10, np.nan, 14, 16, 18]
    })

    handler = MissingDataHandler(df)
    df = handler.handle_missing_values('A', method="median")
    assert df["A"].isnull().sum() == 0  # No missing value in 'B'
    assert df.loc[2, "A"] == df["A"].median()  # Check if missing value was replaced with median


def test_handle_missing_values_mode():
    df = pd.DataFrame({
        'A': [1, 2, 2, np.nan, 5],
        'B': ['x', 'y', 'y', np.nan, 'x']
    })
    handler = MissingDataHandler(df)
    df = handler.handle_missing_values("B", method="mode")
    assert df['B'].isnull().sum() == 0  # No missing values in 'B'
    assert df.loc[3, 'B'] == 'x'  # Mode of B is 'y'


def test_handle_missing_invalid_method(handler_instance):
    with pytest.raises(ValueError, match="Invalid method. Choose from 'drop',"
                                         " 'mean', 'median', 'mode', or 'custom'."):
        handler_instance.handle_missing_values("A", method="invalid")


if __name__ == "__main__":
    pytest.main()