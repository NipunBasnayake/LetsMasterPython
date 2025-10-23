import numpy as np

# Create a 1-dimensional array
arr_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:")
print(arr_1d)

# Create a 2-dimensional array (matrix)
arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
print("\n2D Array:")
print(arr_2d)

# Create a 3-dimensional array
arr_3d = np.array([[[1, 2, 3],
                    [4, 5, 6],
                    [1, 2, 3],
                    [4, 5, 6]]])
print("\n3D Array:")
print(arr_3d)

# Create an array with at least 5 dimensions using ndmin
arr = np.array([1, 2, 3, 4], ndmin=5)
print("\nArray with minimum 5 dimensions:")
print(arr)
print("Number of dimensions:", arr.ndim)
