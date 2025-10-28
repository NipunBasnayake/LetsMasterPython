import pandas as pd

# Read the CSV (Comma-Separated Values) file named 'data.csv'
# This function loads the data into a DataFrame (a table-like data structure)
df = pd.read_csv('data.csv')

# Display the first 2 rows of the DataFrame
# Useful for quickly checking the top portion of your data
print(df.head(2))

# Display the first 5 rows (default value for head())
# Helps to get an overview of the data structure and column names
print(df.head())

# Display the last 5 rows of the DataFrame
# Helps to inspect the end of the dataset
print(df.tail())

# Display detailed information about the DataFrame
# Shows column names, data types, and non-null counts
print(df.info())
