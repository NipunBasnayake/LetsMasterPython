# 1. Removing duplicates from a list using set
def unique_elements(input_list):
    return set(input_list)

my_list = [1, 2, 2, 3, 4, 5]
result_set = unique_elements(my_list)
print("1. Unique elements:", result_set)


# 2. Finding common elements between two sets
def common_elements(set1, set2):
    return set1.intersection(set2)

set_A = {1, 2, 3, 4, 5}
set_B = {3, 4, 5, 6, 7}
result_set = common_elements(set_A, set_B)
print("2. Common elements:", result_set)


# 3. Finding difference between two sets
def set_difference(set3, set4):
    return set3.difference(set4)

set_C = {1, 2, 3, 4, 5}
set_D = {3, 4, 5, 6, 7}
result_set = set_difference(set_C, set_D)
print("3. Difference elements:", result_set)


# 4. Checking if one set is a subset of another
def is_subset(set5, set6):
    return set5.issubset(set6)

set_E = {1, 2, 3, 4, 5}
set_F = {3, 4, 5, 6, 7}
result_bool = is_subset(set_E, set_F)
print("4. Is subset:", result_bool)
