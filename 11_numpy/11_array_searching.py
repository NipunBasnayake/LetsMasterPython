import numpy as np

# Create a 1D NumPy array
original_1d_array = np.array([1, 2, 3, 6, 7, 8, 4, 3, 2])

# Find indices where the value is equal to 2
result1 = np.where(original_1d_array == 2)

# Extract elements greater than 4 (Boolean indexing)
result2 = original_1d_array[original_1d_array > 4]

# Extract elements greater than 4 using np.extract()
result3 = np.extract(original_1d_array > 4, original_1d_array)

# Print results
print(result1)  # Tuple of indices where condition is True
print(result2)  # Elements greater than 4
print(result3)  # Same result as result2
