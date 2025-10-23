import numpy as np

# Create a 1D array
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# Slice from index 2 to 5 (6 is exclusive)
slice_result = arr[2:6]
print("1D slice (index 2 to 5):", slice_result)  # [2 3 4 5]

# Create a 2D array (4x4)
arr_2d = np.array([[0, 1, 2, 3],
                   [4, 5, 6, 7],
                   [8, 9, 10, 11],
                   [12, 13, 14, 15]])

# Slice rows 1 to 2 (3 is exclusive) and all columns
slice_result_2d = arr_2d[1:3, :]  # ":" means all columns
print("2D slice (rows 1-2, all columns):")
print(slice_result_2d)
