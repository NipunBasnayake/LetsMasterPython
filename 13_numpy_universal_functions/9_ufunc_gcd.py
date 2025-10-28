import numpy as np

# Find GCD of all numbers in the list using NumPy reduce
gcd_result = np.gcd.reduce([12, 30, 45, 60])
print("Greatest Common Divisor:", gcd_result)

# Create a custom universal function (ufunc) for GCD
custom_gcd = np.frompyfunc(lambda x, y: np.gcd(x, y), 2, 1)

# Use the custom ufunc to find GCD of multiple elements
custom_gcd_result = custom_gcd.reduce([24, 56, 93, 16, 75, 25])
print("Custom GCD:", custom_gcd_result)

# Another example using an array
arr = np.array([12, 30, 45, 60])
x = np.gcd.reduce(arr)
print("GCD of array elements:", x)
