import numpy as np

# Create a 1D array
arr = np.array([0, 1, 2, 3, 4])

# Access elements using positive and negative indexing
print("Element at index 2:", arr[2])  # 3rd element (value 2)
print("Last element:", arr[-1])  # Last element (value 4)

# Boolean indexing: get elements greater than 2
mask = arr > 2
print("Elements greater than 2:", arr[mask])  # [3, 4]

# Create a 2D array (matrix)
arr_2d = np.array([[0, 1, 2],
                   [3, 4, 5],
                   [6, 7, 8]])

# Access elements in 2D array
print("Element at row 1, column 2:", arr_2d[1, 2])  # 2nd row, 3rd column -> 5
print("Element at row 0, last column:", arr_2d[0, -1])  # 1st row, last column -> 2
