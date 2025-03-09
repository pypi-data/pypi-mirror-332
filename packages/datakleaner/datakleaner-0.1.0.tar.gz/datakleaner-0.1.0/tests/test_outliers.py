# Import the necessary libraries
import pytest
import pandas as pd
from datakleaner.outliers import OutlierHandler


@pytest.fixture
def sample_dataframe():
    data = {
        'A': [1, 2, 3, 100, 5, 6],  # Outlier at 100
        'B': [10, 12, 14, 16, 18, 200],  # Outlier at 200
        'C': [5, 7, 9, 11, 13, 15]  # No outliers
    }
    return pd.DataFrame(data)


@pytest.fixture
def handler_instance(sample_dataframe):
    return OutlierHandler(sample_dataframe)


def test_remove_outliers(handler_instance):
    handler_instance.handle_outliers(strategy="remove")
    assert handler_instance.df.shape[0] < 6  # Rows should be removed if outliers exist


def test_impute_outliers(handler_instance):
    handler_instance.handle_outliers(strategy="impute", method="median")
    assert handler_instance.df.loc[3, "A"] != 100  # Outlier should be replaced
    assert handler_instance.df.loc[5, "B"] != 200  # Outlier should be replaced


def test_invalid_outlier_strategy(handler_instance):
    with pytest.raises(ValueError, match="Invalid strategy. Choose 'remove' or 'impute'."):
        handler_instance.handle_outliers(strategy="invalid")


def test_invalid_outlier_method(handler_instance):
    with pytest.raises(ValueError, match="Invalid method. Choose 'mean', 'median', or 'mode'."):
        handler_instance.handle_outliers(strategy="impute", method="invalid")

if __name__ == "__main__":
    pytest.main()
