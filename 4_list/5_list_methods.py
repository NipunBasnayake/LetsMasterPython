# 1. Inserting an element at a specific position
my_list = ['math', 'chemistry', 1997, 2000]
my_list.insert(2, 10087)  # Insert 10087 at index 2
print("After insert:", my_list)

# 2. Counting occurrences and finding index
list1 = [1, 2, 3, 1, 2, 3, 4, 5, 6, 3, 2, 1, 3]
print("Count of 1:", list1.count(1))  # Count occurrences of 1
print("Index of first 3:", list1.index(3))  # Index of first 3

# 3. Sorting a list in descending order
list3 = [2.3, 4.5, 6.7, 8.9]
list3.sort(reverse=True)
print("Sorted descending:", list3)

# 4. Removing and returning the last element
list4 = [1, 2, 3, 4, 5]
print("Popped element:", list4.pop())
print("List after pop:", list4)

# 5. Removing a specific element
list5 = [1, 2, 3, 4, 5]
list5.remove(3)  # Remove the first occurrence of 3
print("After remove:", list5)
