# 1. Simple squares
squares = [x ** 2 for x in range(5)]
print(squares)

# 2. Even squares
even_squares = [x ** 2 for x in range(10) if x % 2 == 0]
print(even_squares)

# 3. Flattening a matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_matrix = [num for row in matrix for num in row]
print(flattened_matrix)

# 4. Conditional list comprehension
numbers = [1, 2, 3, 4, 5]
squared_numbers = [x**2 if x % 2 == 0 else x for x in numbers]
print(squared_numbers)

# 5. Doubling numbers
double_numbers = [x * 2 for x in range(10)]
print(double_numbers)
