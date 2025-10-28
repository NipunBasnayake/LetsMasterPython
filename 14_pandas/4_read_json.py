import pandas as pd

# Define the file path of the JSON file to be read
# Make sure 'team.json' exists in the same directory as this Python script
file_path = 'team.json'

# Read the JSON file and store its content into a DataFrame
# pd.read_json() automatically converts JSON data into a table-like structure
df = pd.read_json(file_path)

# Print a message to indicate that the data has been successfully read
print("DataFrame from JSON file:")

# Display the content of the DataFrame on the console
print(df)
