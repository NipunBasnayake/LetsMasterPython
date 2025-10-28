import pandas as pd

# 1️⃣ Creating a DataFrame from a dictionary of lists
data_dict = {
    'Name': ['John', 'Jane', 'Jenny'],
    'Age': [36, 24, 33],
    'City': ['New York', 'Paris', 'London']
}

df_from_dict = pd.DataFrame(data_dict)

print("DataFrame from Dictionary of Lists:")
print(df_from_dict)
print("\n")  # Blank line for readability

# 2️⃣ Creating a DataFrame from a list of dictionaries
data_list_of_dict = [
    {'Name': 'John', 'Age': 36, 'City': 'New York'},
    {'Name': 'Jane', 'Age': 24, 'City': 'Paris'},
    {'Name': 'Jenny', 'Age': 33, 'City': 'London'}
]

df_from_list_of_dict = pd.DataFrame(data_list_of_dict)

print("DataFrame from List of Dictionaries:")
print(df_from_list_of_dict)
print("\n")  # Blank line for readability

# 3️⃣ Creating a Series from a list
data_list = [10, 20, 30, 40, 50]
data_series = pd.Series(data_list)
print("Series from a list:")
print(data_series)
print("\n")

# 4️⃣ Creating a Series from a dictionary
data_dict_series = {'a': 10, 'b': 20, 'c': 30}
data_series_2 = pd.Series(data_dict_series)
print("Series from a dictionary:")
print(data_series_2)
