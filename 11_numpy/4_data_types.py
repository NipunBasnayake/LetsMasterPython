import numpy as np

# Create arrays of different types
arr_int = np.array([1, 2, 3, 4])  # Integer array
arr_float = np.array([1.0, 2.1, 3.2, 4.3])  # Float array
arr_complex = np.array([1 + 2j, 3 + 4j, 5 + 6j])  # Complex array

# Check the data type of each array
print("Data type of arr_int:", arr_int.dtype)  # int64 (or int32 depending on system)
print("Data type of arr_float:", arr_float.dtype)  # float64
print("Data type of arr_complex:", arr_complex.dtype)  # complex128

# Explicitly set the data type while creating array
arr_explicit_int = np.array([1, 2, 3], dtype=np.int32)
print("Explicit int32 array dtype:", arr_explicit_int.dtype)

# Explicitly set complex data type
arr_complex64 = np.array([1 + 2j, 3 + 4j], dtype=np.complex64)
print("Explicit complex64 array dtype:", arr_complex64.dtype)
