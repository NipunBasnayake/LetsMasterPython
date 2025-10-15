# 1. Original dictionary
original_dictionary = {'name': 'John', 'age': 36, 'city': 'New York'}

# 2. Copying using copy() method
copied_dictionary_1 = original_dictionary.copy()
print("Copied dictionary 1:", copied_dictionary_1)

# 3. Copying using dict() constructor
copied_dictionary_2 = dict(original_dictionary)
print("Copied dictionary 2:", copied_dictionary_2)

# 4. Nested dictionary example
original_dictionary_2 = {
    'person': {
        'name': 'John',
        'age': 36,
        'city': 'New York'
    }
}
print("Nested dictionary:", original_dictionary_2)
