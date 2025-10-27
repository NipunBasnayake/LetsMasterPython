import numpy as np

# Create two NumPy arrays
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([6, 7, 8, 9, 10])

# Perform element-wise arithmetic operations using NumPy ufuncs (universal functions)

# Adds corresponding elements of array1 and array2
add_result = np.add(array1, array2)

# Subtracts elements of array2 from array1
sub_result = np.subtract(array1, array2)

# Multiplies corresponding elements
mul_result = np.multiply(array1, array2)

# Divides elements of array1 by elements of array2
div_result = np.divide(array1, array2)

# Finds the remainder (modulus) of each division
mod_result = np.mod(array1, array2)

# Multiplies each element of array1 by a scalar value (2)
scalar_multiply = np.multiply(array1, 2)

# Display the results
print("Addition:", add_result)
print("Subtraction:", sub_result)
print("Multiplication:", mul_result)
print("Division:", div_result)
print("Modulus:", mod_result)
print("Scalar Multiplication:", scalar_multiply)
