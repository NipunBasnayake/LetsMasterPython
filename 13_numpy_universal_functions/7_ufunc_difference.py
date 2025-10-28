import numpy as np

# Create an array of numbers
data_array = np.array([10, 20, 30, 40, 50, 60])

# Compute the difference between consecutive elements
difference_result = np.diff(data_array)
print("Difference between consecutive elements:", difference_result)
# → [10, 10, 10, 10, 10]
# Explanation: (20−10), (30−20), (40−30), (50−40), (60−50)

# Compute the difference along axis 0 (for 1D, same as above)
axis_difference_result = np.diff(data_array, axis=0)
print("Difference along axis 0:", axis_difference_result)

# Create another array
array = np.array([10, 55, 86, 24, 59])

# Compute the 2nd-order difference (difference of differences)
new_array = np.diff(array, n=2)
print("2nd-order difference:", new_array)
# First diff → [45, 31, -62, 35]
# Second diff → [-14, -93, 97]
