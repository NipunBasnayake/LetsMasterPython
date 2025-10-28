import pandas as pd

# 1️⃣ Creating a Series from a list with custom indices
a = [2, 3, 4]
my_variable = pd.Series(a, index=['a', 'b', 'c'])
print(my_variable)
# Output:
# a    2
# b    3
# c    4
# dtype: int64
# → Each element from the list is assigned a label (index) from ['a','b','c']

# 2️⃣ Creating a Series from a simple list (default integer indices)
data_list = [10, 20, 30, 40, 50]
data_series = pd.Series(data_list)
print(data_series)
# Output:
# 0    10
# 1    20
# 2    30
# 3    40
# 4    50
# dtype: int64
# → If no index is specified, Pandas automatically assigns integer indices starting from 0

# 3️⃣ Creating a Series from a dictionary
data_dict = {'a': 10, 'b': 20, 'c': 30}
data_series_2 = pd.Series(data_dict)
print(data_series_2)
# Output:
# a    10
# b    20
# c    30
# dtype: int64
# → Keys of the dictionary become the index, and values become the data
