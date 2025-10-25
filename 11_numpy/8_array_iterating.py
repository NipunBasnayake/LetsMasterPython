import numpy as np

# 1D array iteration
my_array = np.array([1, 2, 3, 4, 5])
for element in my_array:
    print(element)  # Prints each element individually: 1, 2, 3, 4, 5

# 2D array iteration (row-wise)
my_2d_array = np.array([[1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9]])

for row in my_2d_array:
    print("Row:", row)  # Prints the entire row
    for element in row:
        print(" Element:", element)  # Prints each element in the row

# Using np.nditer to iterate over all elements in a multi-dimensional array
for element in np.nditer(my_2d_array):
    print(element)  # Prints all elements one by one: 1, 2, 3, 4, 5, 6, 7, 8, 9
