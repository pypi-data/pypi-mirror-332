# Import the necessary libraries
import pytest
import pandas as pd
from datakleaner.duplicates import DuplicateHandler


@pytest.fixture
def sample_dataframe():
    data = {
        'A': [1, 2, 2, 3, 4, 4, 5],  # Duplicates in A
        'B': ['x', 'y', 'y', 'z', 'w', 'w', 't'],  # Duplicates in B
        'C': [10, 20, 20, 30, 40, 40, 50]  # Duplicates in C
    }
    return pd.DataFrame(data)


@pytest.fixture
def handler_instance(sample_dataframe):
    return DuplicateHandler(sample_dataframe)


def test_remove_duplicates(handler_instance):
    handler_instance.remove_duplicates()
    assert handler_instance.df.duplicated().sum() == 0  # No duplicates should remain


if __name__ == "__main__":
    pytest.main()