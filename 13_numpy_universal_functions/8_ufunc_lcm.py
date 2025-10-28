import numpy as np

# Create an array of numbers
numbers = np.array([12, 30, 45, 60])

# Calculate the LCM (Least Common Multiple) of all elements in the array
lcm_result = np.lcm.reduce(numbers)
print("LCM of all numbers:", lcm_result)

# Use a custom universal function (ufunc) to find LCM pairwise
custom_lcm = np.frompyfunc(lambda x, y: np.lcm(x, y), 2, 1)
custom_lcm_result = custom_lcm(numbers, numbers)
print("Custom LCM of all numbers:", custom_lcm_result)

# Another array example
arr = np.array([3, 6, 9, 12])
x = np.lcm.reduce(arr)
print("LCM of array elements:", x)
