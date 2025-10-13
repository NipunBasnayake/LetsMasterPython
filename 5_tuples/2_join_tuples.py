# 1. Concatenating tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
result_tuple = tuple1 + tuple2
print("Concatenated tuple:", result_tuple)

# 2. Repeating a tuple
result_tuple = tuple1 * 2
print("Repeated tuple:", result_tuple)

# 3. Zipping two tuples together
names = ('Nipun', 'Sagar', 'Suresh')
ages = (20, 21, 22)
result_tuple = list(zip(names, ages))  # Converts zipped pairs into a list of tuples
print("Zipped tuple:", result_tuple)
