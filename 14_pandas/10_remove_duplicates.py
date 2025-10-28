import pandas as pd

# Sample data containing potential duplicates
data_with_duplicates = {
    'ProductID': ['P01', 'P02', 'P03', 'P04', 'P05'],
    'Quantity': [10, 15, 30, 30, 60]  # Note: '30' appears twice, could lead to duplicates
}

# Create a DataFrame from the dictionary
df_with_duplicates = pd.DataFrame(data_with_duplicates)

# Detect duplicate rows
# df.duplicated() returns a boolean Series indicating which rows are duplicates
# By default, it marks all except the first occurrence as True
duplicates_rows = df_with_duplicates[df_with_duplicates.duplicated()]
print("Duplicate rows:")
print(duplicates_rows)
# Special thing: This only shows rows considered duplicates, not the first occurrence

# Remove duplicate rows
# drop_duplicates() removes all duplicates and keeps the first occurrence by default
df_without_duplicates = df_with_duplicates.drop_duplicates()
print("\nDataFrame after removing duplicates:")
print(df_without_duplicates)
# Special thing: You can also use keep='last' or keep=False to control which duplicates are removed

# Find rows that are duplicates considering the first occurrence
# keep='first' marks duplicates as True except the first occurrence
df_first_occurrences = df_with_duplicates[df_with_duplicates.duplicated(keep='first')]
print("\nFirst occurrences:")
print(df_first_occurrences)
# Special thing: Here, you can see which rows are considered duplicates excluding the first instance
