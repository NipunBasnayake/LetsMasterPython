import numpy as np

# Create a 1D array
original_1d_array = np.array([1, 2, 3, 4, 5, 6])

# Split the array into 2 equal parts
result1 = np.split(original_1d_array, 2)
# Output: [array([1, 2, 3]), array([4, 5, 6])]

# Split at specific positions (index 2 and 4)
result2 = np.split(original_1d_array, [2, 4])
# Output: [array([1, 2]), array([3, 4]), array([5, 6])]

print(result1)
print(result2)

# Create a 2D array
original_2d_array = np.array([[1, 2, 3],
                              [4, 5, 6]])

# Split the 2D array into 3 equal parts along columns (axis=1)
result3 = np.split(original_2d_array, 3, axis=1)
# Output: [array([[1], [4]]), array([[2], [5]]), array([[3], [6]])]

print(result3)
