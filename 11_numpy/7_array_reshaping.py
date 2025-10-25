import numpy as np

# Original 1D array
original_array = np.array([1, 2, 3, 4, 5, 6])

# Reshape using row-major order (C-style)
row_major = original_array.reshape(2, 3, order='C')  # Fill rows first

# Reshape using column-major order (Fortran-style)
column_major = original_array.reshape(2, 3, order='F')  # Fill columns first

# Print the arrays
print("Original array:\n", original_array)
print("Reshaped array (row-major order):\n", row_major)
print("Reshaped array (column-major order):\n", column_major)
