import numpy as np

# 1D array
array_1d = np.array([1, 2, 3, 4, 5])
# 2D array (2 rows, 3 columns)
array_2d = np.array([[1, 2, 3],
                     [4, 5, 6]])
# 3D array (2 blocks, each with 2 rows and 2 columns)
array_3d = np.array([[[1, 2], [3, 4]],
                     [[5, 6], [7, 8]]])

# Print shapes
print("Shape of 1D array:", array_1d.shape)  # (5,) → 1 row with 5 elements
print("Shape of 2D array:", array_2d.shape)  # (2, 3) → 2 rows, 3 columns
print("Shape of 3D array:", array_3d.shape)  # (2, 2, 2) → 2 blocks, each 2x2
