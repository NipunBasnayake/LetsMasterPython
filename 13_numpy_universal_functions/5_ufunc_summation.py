import numpy as np

# Create a NumPy array
data_array = np.array([10, 20, 30, 40, 50])

# Calculate the sum of all elements
sum_result = np.sum(data_array)
print("Summation Result:", sum_result)

# Axis sum (for 1D array, same as total sum)
axis_sum_result = np.sum(data_array, axis=0)
print("Summation along axis:", axis_sum_result)

# Example of using a custom function (e.g., cumulative sum)
array = np.array([1, 2, 3, 4, 5])
new_array = np.cumsum(array)  # <-- np.custom does not exist
print("Cumulative Sum Array:", new_array)
