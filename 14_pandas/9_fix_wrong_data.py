import pandas as pd

# Data containing wrong (non-numeric) values
data_wrong = {
    'ProductId': ['P001', 'P002', 'P003'],
    'Quantity': ['10', '15', '22a']
}

# Create DataFrame
df_wrong = pd.DataFrame(data_wrong)

# Detect rows where 'Quantity' contains non-numeric values
wrong_data_rows = df_wrong[~df_wrong['Quantity'].str.isnumeric()]
print("Identifying wrong data:")
print(wrong_data_rows)

# Fix wrong data by keeping only numeric part
df_wrong['Quantity'] = df_wrong['Quantity'].str.extract('(\d+)')

# Convert the column to numeric type
df_wrong['Quantity'] = pd.to_numeric(df_wrong['Quantity'])

print("\nFixed DataFrame:")
print(df_wrong)
