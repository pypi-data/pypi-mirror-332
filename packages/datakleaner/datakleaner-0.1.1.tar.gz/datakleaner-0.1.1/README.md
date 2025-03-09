# DataKleaner

## Overview
**DataKleaner** is an open-source Python package designed to automate data cleaning tasks, including checking and handling missing values, detecting and removing duplicate records, and identifying and treating outliers. 

It is built with **pandas**, **numpy**, **matplotlib** and **scipy** to facilitate efficient data preprocessing for analysis and machine learning.

## Features
- **Data Diagnosis**: Generates a summary report of missing values, duplicates, and outliers at a go.
- **Outlier Visualisation**: Creates beautiful box plots to show where and what the outliers are.
- **Missing Data Handling**: Identifies and handles missing values by dropping or imputing them.
- **Duplicate Detection and Removal**: Detects and cleans duplicate rows in a dataset.
- **Outlier Detection and Treatment**: Identifies and handles outliers using IQR and Z-score methods.

## Installation
```sh
pip install datakleaner
```
Or install from source:
```sh
git clone https://github.com/olivetahonsu/datakleaner.git
cd datakleaner
pip install -e .
```

## Usage
### Import the package
```python
import pandas as pd
from datakleaner.missing_data import MissingDataHandler
from datakleaner.duplicates import DuplicateHandler
from datakleaner.outliers import OutlierHandler
from datakleaner.diagnosis import Diagnoser
```

### Diagnosing Data Issues
```python
data = {
       'A': [1, 2, 100, 1, 5, np.nan],  # Outlier at 100, Missing value
       'B': [10, 12, 14, 10, 18, 200],  # Outlier at 200
       'C': [5, 7, 9, 5, 13, 15],
       'D': ['x', 'y', 'y', 'x', 'w', 'w']}

df = pd.DataFrame(data)

diagnoser = Diagnoser(df)
diagnoser.generate_report()

# You can check each of missing_values, duplicates and outliers separately.
diagnoser.check_duplicates() # To view only the duplicates rows.

diagnoser.check_missing_values() # To check if there is any column with missing values.

diagnoser.check_outliers() # To check if there is any column with outliers.
```
By default, **.check_outliers()** uses Inter-quarter Range (IQR) method to look for outliers.

You can use the statistical method, **Z-score** to check for outliers if your data follows a normal distribution.

This is how to implement **.check_outliers()** to use Z-score: 

```python
outliers = diagnoser.check_outliers(method="zscore", threshold=3)
print(outliers)
```
Note: The default **threshold** is 3. You can omit it or specify yours.

### Handling Missing Data
```python
data = {
       'A': [1, 2, np.nan, 4, 5],
       'B': [np.nan, 1, 2, 3, np.nan],
       'C': [10, 20, 30, 40, 50]}

df = pd.DataFrame(data)

handler = MissingDataHandler(df)
cleaned_df = handler.handle_missing_values(column=['A', 'B'], method="mean")
print(cleaned_df)
```
The **method** argument can be any of these:

- **drop** : This will drop missing values from a column you specified. You have to specify **just a column** here, 
not a list of columns.
- **mean** : This will replace the missing values with the mean of the column.
- **median** : It replaces the missing values with the median of the column.
- **mode** : The missing values are replaced by the mode of the column.
- **custom** : The missing values are replaced by a custom value you specify. For this, you have to include 
a third argument **custom_value** and set it to a value of your choice depending on your dataset. 
### Handling Duplicates
```python
data = {
       'A': [1, 2, 2, 3, 4, 4, 4, 5],
       'B': ['x', 'y', 'y', 'z', 'w', 'w', 'w', 'v']}

df = pd.DataFrame(data)

handler = DuplicateHandler(df)
cleaned_df = handler.remove_duplicates(keep='first')
print(cleaned_df)
```
There are three options for the **keep** argument:

- **first** : This retains the first instance or occurrence of the duplicates while dropping all others.
- **last** : This retains the last occurrence of the duplicates while removing all others.
- **none** : This remove all instances of the duplicates.

### Handling Outliers
```python
data = {
       "A": [1, 2, 3, 6, 5, 100],  # Outlier at index 5
       "B": [10, 12, 14, 16, 18, 200],  # Outlier at index 5
       "C": [5, 7, 9, 11, 13, 15],}

df = pd.DataFrame(data)

handler = OutlierHandler(df)

handler.visualise_outliers() # Creates box plots of the numeric columns to show where the outliers are.

cleaned_df = handler.handle_outliers(strategy="impute", check_type="zscore", threshold=2)
print(cleaned_df)
```
The **.handle_outliers()** method can take up to four arguments. But when you call it without specifying an argument,
it just removes all outliers.

The following are the arguments it can take:

- **strategy** : This can either be **"remove"**, which is the default, or **"impute"**.
- **method** : It is what the **datakleaner** will use to replace your outliers. It can either be **"mean"**, **"median"**,
or **"mode"**. You need to specify this argument when you choose **strategy** to be **"impute"**.
- **check_type** : It can either be **"iqr**", for inter-quarter range, or **"zscore"**. It dictates how the **datakleaner** 
will check the outliers in your dataset.
- **threshold** : It is needed when your **check_type** is **"zscore"**. If you don't specify it, the
**datakleaner** will use 3 as the default value.

## Running Tests
Run tests using `pytest`:
```sh
pytest tests/
```

## Contributing
1. Fork the repository.
2. Create a new branch (`feature-branch`).
3. Commit your changes.
4. Push to your branch and open a Pull Request.

## License
This project is licensed under the **Apache 2.0 License**.

## Contact
For questions or suggestions, open an issue at:
[GitHub Issues](https://github.com/olivetahonsu/datakleaner).
Email: olivetahonsu@gmail.com
