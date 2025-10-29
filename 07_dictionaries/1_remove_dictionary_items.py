# 1. Deleting a specific key-value pair using del
my_dict_1 = {'name': 'John', 'age': 36, 'city': 'New York'}
del my_dict_1['age']  # Removes the key 'age' and its value
print("After del:", my_dict_1)

# 2. Removing and returning a value using pop()
my_dict_2 = {'name': 'John', 'age': 36, 'city': 'New York'}
removed_city = my_dict_2.pop('city')  # Removes 'city' and returns its value
print("Removed value (city):", removed_city)
print("After pop():", my_dict_2)

# 3. Clearing all key-value pairs using clear()
my_dict_3 = {'name': 'John', 'age': 36, 'city': 'New York'}
my_dict_3.clear()  # Removes all items from the dictionary
print("After clear():", my_dict_3)
