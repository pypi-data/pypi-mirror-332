# Import the necessary libraries
import pytest
import pandas as pd
import numpy as np
from datakleaner.diagnosis import Diagnoser


@pytest.fixture
def sample_dataframe():
    data = {
        'A': [1, 2, np.nan, 4, 5, 100],  # Outlier at 100, Missing value
        'B': [10, 12, 14, 16, 18, 200],  # Outlier at 200
        'C': [5, 7, 9, 11, 13, 15],
        'D': ['x', 'y', 'y', 'z', 'w', 'w']
    }

    return pd.DataFrame(data)


@pytest.fixture
def diagnoser_instance(sample_dataframe):
    return Diagnoser(sample_dataframe)


def test_check_missing_values(diagnoser_instance):
    missing_values = diagnoser_instance.check_missing_values()
    assert "A" in missing_values  # Column 'A' has missing values
    assert missing_values["A"] == 1   # Only one missing value


def test_check_duplicates():
    df = pd.DataFrame({
        'A': [1, 2, 2, 3, 4, 4],
        'B': ['x', 'y', 'y', 'z', 'w', 'w']
    })

    diagnoser = Diagnoser(df)
    duplicate_count = diagnoser.check_duplicates()
    assert duplicate_count == 2 # Two duplicate rows


def test_check_outliers(diagnoser_instance):
    outliers = diagnoser_instance.check_outliers(method="iqr")
    assert "A" in outliers # Column 'A' has outliers
    assert "B" in outliers # Column 'B' has outliers


def test_generate_report(diagnoser_instance, capsys):
    diagnoser_instance.generate_report()
    captured = capsys.readouterr()
    assert "Missing Values:" in captured.out
    assert "Duplicate Rows:" in captured.out
    assert "Outliers Found:" in captured.out


if __name__ == "__main__":
    pytest.main()

