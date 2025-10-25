import numpy as np

# -------------------------
# 1D Array Example
# -------------------------
original_array = np.array([10, 20, 30, 40, 50])

# Create a view (shallow copy) of the original array
array_view = original_array.view()

# Create a deep copy of the original array
copied_array = np.copy(original_array)

# Modify the copied array
copied_array[0] = 99

# Print arrays
print("Original 1D array:", original_array)  # Remains unchanged
print("View of 1D array:", array_view)       # Also unchanged
print("Copied 1D array:", copied_array)      # First element changed

# -------------------------
# 2D Array Example
# -------------------------
original_2d_array = np.array([[1, 2, 3],
                              [4, 5, 6],
                              [7, 8, 9]])

# Create a view of the 2D array
array_2d_view = original_2d_array.view()

# Create a deep copy of the 2D array
array_2d_copy = np.copy(original_2d_array)

# Modify the view
array_2d_view[0, 0] = 88

# Print arrays
print("Original 2D array after modifying the view:\n", original_2d_array)
print("View of 2D array:\n", array_2d_view)   # Shares memory with original array
print("Copied 2D array:\n", array_2d_copy)   # Remains unchanged
