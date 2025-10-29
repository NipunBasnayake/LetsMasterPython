# 1. Copying lists correctly and incorrectly
original_list = [1, 2, 3, 4, 5]

# Method 1: Using list() constructor
copied_list_1 = list(original_list)

# Method 2: Using copy() method
copied_list_2 = original_list.copy()

# Incorrect way: just assigning (both variables point to the same list)
incorrect_copy = original_list

# Printing results
print("Incorrect copy (shared reference):", incorrect_copy)
print("Copied list using list():", copied_list_1)
print("Copied list using copy():", copied_list_2)
