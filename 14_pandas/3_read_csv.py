import pandas as pd

# Step 1: Specify the CSV file path
file_path = 'data.csv'

# Step 2: Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Step 3: Display the DataFrame
print("DataFrame from CSV file:")
print(df)

# Step 4: Check current maximum number of rows displayed
print("Current max rows display:", pd.options.display.max_rows)

# Step 5: Increase max rows displayed (optional)
pd.options.display.max_rows = 999

# Step 6: Read the CSV again (optional, just to reflect updated display option)
df = pd.read_csv(file_path)
print("DataFrame with updated max rows display:")
print(df)
