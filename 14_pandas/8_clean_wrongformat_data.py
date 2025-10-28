import pandas as pd

# Data with wrong formats
data_wrong_formats = {
    'ProductId': ['P001', 'P002', 'P003', 'P004'],
    'Price': ['50.25$', '39.15$', '88.25$', '61.85$']
}

# Create DataFrame
df_wrong_formats = pd.DataFrame(data_wrong_formats)

# Detect wrong formats (values containing '$')
wrong_formats_info = df_wrong_formats['Price'].apply(lambda x: '$' in x)

print("DataFrame with wrong formats:")
print(df_wrong_formats)

print("\nWrong format info (True means format issue):")
print(wrong_formats_info)

# ✅ Clean the 'Price' column by removing the '$' symbol and converting to float
df_wrong_formats['Price'] = df_wrong_formats['Price'].str.replace('$', '', regex=False).astype(float)

print("\nCleaned DataFrame (symbols removed, values converted to float):")
print(df_wrong_formats)
