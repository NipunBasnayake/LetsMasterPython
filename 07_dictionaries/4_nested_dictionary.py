# 1. Creating a nested dictionary
person = {
    'name': 'Nipun',
    'age': 25,
    'address': {
        'city': 'New York',
        'zipcode': '12345'
    }
}

# 2. Printing the full nested dictionary
print("Nested dictionary:", person)

# 3. Accessing a value from the nested dictionary
city = person['address']['city']
print(f"City: {city}")

# 4. Updating a value inside the nested dictionary
person['address']['zipcode'] = '10001'
print("Updated dictionary:", person)
