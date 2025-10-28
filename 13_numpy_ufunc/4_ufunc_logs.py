import numpy as np

# Create a NumPy array of numbers
numbers_array = np.array([1, 2, 3, 4, 5])

# Apply the natural logarithm (base e)
logarithmic_result = np.log(numbers_array)
print("Logarithmic result:", logarithmic_result)

# Apply the exponential function (e^x)
exponential_result = np.exp(numbers_array)
print("Exponential result:", exponential_result)

# Apply the base-10 logarithm
log_base_10_result = np.log10(numbers_array)
print("Log base 10 result:", log_base_10_result)
