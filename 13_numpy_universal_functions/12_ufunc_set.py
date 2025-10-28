import numpy as np

# 1️⃣ Find unique elements in an array
arr = np.array([1, 2, 1, 4, 5, 2, 4, 6, 7])
x = np.unique(arr)
print(x)
# Output: [1 2 4 5 6 7] → all unique elements sorted

# 2️⃣ Union of two arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([3, 4, 2, 5, 6, 7, 8])
new_arr = np.union1d(arr1, arr2)
print(new_arr)
# Output: [1 2 3 4 5 6 7 8] → all elements from both arrays, sorted and unique

# 3️⃣ Intersection of two arrays
new_arr1 = np.intersect1d(arr1, arr2, assume_unique=True)
print(new_arr1)
# Output: [2 3 4 5] → elements common to both arrays

# 4️⃣ Set difference (elements in arr1 not in arr2)
new_arr3 = np.setdiff1d(arr1, arr2)
print(new_arr3)
# Output: [1] → elements only in arr1, not in arr2
