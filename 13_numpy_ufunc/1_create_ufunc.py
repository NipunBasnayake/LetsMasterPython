import numpy as np

# Define a normal Python function that adds two numbers
def add(x, y):
    return x + y

# Convert the Python function 'add' into a NumPy universal function (ufunc)
# np.frompyfunc(function, num_inputs, num_outputs)
# Here, the function takes 2 inputs and returns 1 output
add = np.frompyfunc(add, 2, 1)

# Apply the new ufunc 'add' on two lists element-wise
# It performs addition just like a vectorized NumPy operation
print(add([1, 2, 3, 4], [5, 6, 7, 8]))

# Print the type of NumPy’s built-in 'add' function
print(type(np.add))

# Check if np.add is a ufunc
if type(np.add) == np.ufunc:
    print("add is a ufunc")
else:
    print("add is not a ufunc")
