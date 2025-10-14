# 1. Adding a single element to a set
my_set_1 = {30, 60, 90}
my_set_1.add(100)
print("After add():", my_set_1)

# 2. Adding multiple elements using update()
my_set_2 = {30, 60, 90}
my_set_2.update({10, 20, 50})
print("After update():", my_set_2)

# 3. Removing a specific element using remove()
my_set_3 = {30, 60, 90, 100, 200, 300}
my_set_3.remove(200)  # Raises error if element not found
print("After remove():", my_set_3)

# 4. Removing a specific element using discard()
my_set_4 = {30, 60, 90, 100, 200, 300}
my_set_4.discard(30)  # No error if element not found
print("After discard():", my_set_4)

# 5. Clearing all elements from the set
my_set_5 = {30, 60, 90, 100, 200, 300}
my_set_5.clear()
print("After clear():", my_set_5)
