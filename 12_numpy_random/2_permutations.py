import numpy as np

# Create a 1D array
original_array_1 = np.array([1, 2, 3, 4, 5, 6])

# np.random.shuffle() shuffles the array *in-place* and returns None
np.random.shuffle(original_array_1)
print("Permuted Array:", original_array_1)

# Create a 2D array
original_array_2 = np.array([[1, 2, 3],
                             [4, 5, 6],
                             [7, 8, 9]])

# np.random.permutation() returns a new shuffled array (doesn't change the original)
permuted_rows = np.random.permutation(original_array_2)       # Shuffles rows
permuted_columns = np.random.permutation(original_array_2.T).T  # Shuffles columns

print("Permuted Rows:\n", permuted_rows)
print("Permuted Columns:\n", permuted_columns)
