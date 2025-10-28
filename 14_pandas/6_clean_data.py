import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('data.csv')

# Display the original data (before cleaning)
print("Original Data:")
print(df)

# Remove duplicate rows from the DataFrame
# The 'inplace=True' parameter updates the existing DataFrame directly
df.drop_duplicates(inplace=True)

# Display the cleaned data (after removing duplicates)
print("\nData after removing duplicates:")
print(df)
