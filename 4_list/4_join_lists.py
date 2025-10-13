# 1. Concatenating two lists
list1 = [1, 2, 3]
list2 = ["a", "b", "c"]

joining_list = list1 + list2
print("Joined list:", joining_list)

# 2. Extending a list with another list
extended_list = list1 + [4, 5, 6]
print("Extended list:", extended_list)

# 3. Using extend() to modify the original list
list1.extend(list2)
print("Modified list using extend():", list1)

# 4. Repeating a list multiple times
repeated_list = list1 * 3
print("Repeated list:", repeated_list)
