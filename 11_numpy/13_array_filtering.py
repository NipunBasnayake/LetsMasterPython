import numpy as np

# Create a 1D NumPy array
original_1d_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Define two boolean conditions
condition1 = original_1d_array > 5   # Values greater than 5
condition2 = original_1d_array < 8   # Values less than 8

# Combine conditions using logical AND (&)
combined_condition = condition1 & condition2

# Filter elements that satisfy condition1 (greater than 5)
filtered_1d_array = original_1d_array[condition1]
print("Original array:", original_1d_array)
print("Filtered array (greater than 5):", filtered_1d_array)

# Filter elements that satisfy both conditions (between 5 and 8)
combined_filtered_array = original_1d_array[combined_condition]
print("Combined filtered array (greater than 5 and less than 8):", combined_filtered_array)
