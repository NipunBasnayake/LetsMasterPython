import pandas as pd

# Create a dictionary containing some empty cells
data_with_empty_cells = {
    'name': ['John', 'Jane', 'Jenny'],
    'age': [36, '', 33],
    'city': ['New York', '', 'London']
}

# Convert dictionary to DataFrame
df_with_empty_cells = pd.DataFrame(data_with_empty_cells)

# Replace empty strings ('') with NaN so pandas can recognize them as missing values
df_with_empty_cells.replace('', pd.NA, inplace=True)

# Check which cells are empty (NaN)
empty_cells = df_with_empty_cells.isnull()
print("Empty cells:")
print(empty_cells)

# Drop rows that contain any empty (NaN) values
cleaned_df = df_with_empty_cells.dropna()

print("\nCleaned DataFrame (after removing rows with empty cells):")
print(cleaned_df)
