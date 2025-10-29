# 1. Simple tuple unpacking
def get_coordinates():
    return 10, 20, 30

x, y, z = get_coordinates()
print("Coordinates:", x, y, z)

# 2. Unpacking with * to capture remaining elements
numbers = (1, 2, 3, 4, 5)
first, *rest, last = numbers
print("First:", first, "Rest:", rest, "Last:", last)

# 3. Nested tuple unpacking
nested_tuple = (1, (2, 3), 4)
a, (b, c), d = nested_tuple  # Added 'd' for the last element
print("Nested unpacking:", a, b, c, d)
