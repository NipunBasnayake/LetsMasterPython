# 1. Iterating through dictionary keys
my_dict_1 = {'name': 'John', 'age': 36, 'city': 'New York'}
for key in my_dict_1:
    print("Key:", key)

# 2. Iterating through dictionary values
for value in my_dict_1.values():
    print("Value:", value)

# 3. Iterating through both keys and values
for key, value in my_dict_1.items():
    print(f"Key: {key}, Value: {value}")
