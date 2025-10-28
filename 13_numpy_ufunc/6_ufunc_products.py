import numpy as np

# Create a NumPy array
data_array = np.array([1, 2, 3, 4, 5])

# Calculate the product of all elements
total_product = np.prod(data_array)
print("Total Product of all elements:", total_product)
# 1 × 2 × 3 × 4 × 5 = 120

# Calculate the product along a specific axis (for 1D array, axis=0 is same as total)
axis_product = np.prod(data_array, axis=0)
print("Product along axis 0:", axis_product)

# Calculate the cumulative product
cumulative_product = np.cumprod(data_array)
print("Cumulative Product:", cumulative_product)
# Each element is multiplied by all previous ones → [1, 2, 6, 24, 120]
