# 1. Creating a dictionary
my_dictionary = {"name": "Nipun", "age": 21, "city": "New York"}

# 2. Getting all keys
keys = my_dictionary.keys()
print("Keys:", keys)

# 3. Getting all values
values = my_dictionary.values()
print("Values:", values)

# 4. Getting all key-value pairs
items = my_dictionary.items()
print("Items:", items)

# 5. Accessing a specific value using get()
age = my_dictionary.get("age")
print("Age:", age)

# 6. Removing a key-value pair using pop()
removed_age = my_dictionary.pop("age")
print("Removed age:", removed_age)
print("Dictionary after pop:", my_dictionary)

# 7. Updating the dictionary with new data
new_data = {'age': 31, 'hobby': 'Reading'}
my_dictionary.update(new_data)
print("Updated dictionary:", my_dictionary)
