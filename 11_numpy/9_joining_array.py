import numpy as np

# Create two 1D arrays
array1 = np.array([50, 60, 70])
array2 = np.array([80, 90, 100])

# Combine arrays horizontally (side by side)
result = np.hstack((array1, array2))
print("Horizontal Stack:", result)
# Output: [ 50  60  70  80  90 100]

# Combine arrays vertically (one above the other)
result = np.vstack((array1, array2))
print("Vertical Stack:\n", result)
# Output:
# [[ 50  60  70]
#  [ 80  90 100]]
