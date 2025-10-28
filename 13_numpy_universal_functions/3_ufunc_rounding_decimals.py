import numpy as np

# Create a NumPy array with decimal numbers
decimal_array = np.array([1.2345, 2.3456, 3.4567, 4.5678, 5.6789])

# Round each element to 2 decimal places
rounded_array = np.around(decimal_array, decimals=2)
print("Rounded to 2 decimals:", rounded_array)

# Round each element to the nearest integer (default decimals=0)
around_result = np.around(decimal_array, decimals=1)
print("Rounded to nearest integer:", around_result)
