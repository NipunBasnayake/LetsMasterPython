import numpy as np

# Create a 1D NumPy array
original_1d_array = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5])

# Sort 1D array (no need for axis=1; only valid for 2D arrays)
sorted_array_1 = np.sort(original_1d_array)
print("Sorted 1D array:", sorted_array_1)

# Get indices that would sort the array
indices_1 = np.argsort(original_1d_array)
print("Indices for sorted 1D array:", indices_1)

# Create a 2D array
original_2d_array = np.array([[3, 1, 4],
                              [1, 5, 9],
                              [2, 6, 5]])

# Sort each column (axis=0 → column-wise)
sorted_array_2 = np.sort(original_2d_array, axis=0)
print("Column-wise sorted 2D array:\n", sorted_array_2)

# Get indices that would sort each row (axis=1 → row-wise)
indices_2 = np.argsort(original_2d_array, axis=1)
print("Indices for row-wise sorting:\n", indices_2)
