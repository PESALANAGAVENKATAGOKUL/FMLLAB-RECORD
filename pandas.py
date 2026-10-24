import pandas as pd

# From a Dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Paris', 'London']
}

# Create DataFrame
df = pd.DataFrame(data)

# Viewing data
print("First 5 Rows:")
print(df.head())

print("\nData Information:")
df.info()

print("\nStatistical Summary:")
print(df.describe())
# Selecting a column
ages = df['Age']

print("Ages column:")
print(ages)

print("\n")

# Filtering rows
above_25 = df[df['Age'] > 25]

print("People with Age > 25:")
print(above_25)

print("\n")

# iloc (integer-based)
row_0 = df.iloc[0]

print("First row using iloc (row index 0):")
print(row_0)

print("\n")

# loc (label-based)
specific_val = df.loc[0, 'Name']

print("Name of the person at index 0:")
print(specific_val)
import pandas as pd
import numpy as np

# Create sample dataset with missing values
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [23, np.nan, 22, 28, np.nan],
    "City": ["New York", "London", np.nan, "Paris", "Berlin"]
}

df = pd.DataFrame(data)

# Display original DataFrame
print("Original DataFrame:")
print(df)

print("\n")

# Check for null values
print("Null values count in each column:")
print(df.isnull().sum())

print("\n")

# Drop rows with missing values
df_clean = df.dropna()

print("DataFrame after dropping rows with missing values:")
print(df_clean)

print("\n")

# Fill missing values with 0
df_filled = df.fillna(0)

print("DataFrame after filling missing values with 0:")
print(df_filled)

print("\n")

# Fill missing 'Age' values with mean of the column
df_mean_filled = df.copy()

df_mean_filled["Age"] = df_mean_filled["Age"].fillna(
    df_mean_filled["Age"].mean()
)

print("DataFrame after filling 'Age' with mean value:")
print(df_mean_filled)

print("\n")

# Fill missing 'City' values with 'Unknown'
df_city_filled = df.copy()

df_city_filled["City"] = df_city_filled["City"].fillna("Unknown")

print("DataFrame after filling 'City' with 'Unknown':")
print(df_city_filled)
