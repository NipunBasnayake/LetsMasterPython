# 1. Iterating over a set
my_set_1 = {1, 2, 3, 4, 5}
for item in my_set_1:
    print("Item:", item)

# 2. Iterating with index using enumerating
my_set_2 = {10, 20, 30, 40, 50}
for index, value in enumerate(my_set_2):
    print(f"Index: {index}, Value: {value}")

# 3. Iterating and filtering even numbers
my_set_3 = {1, 2, 3, 4, 5}
for item in my_set_3:
    if item % 2 == 0:
        print(f"Even number: {item}")

# 4. Iterating using while and pop()
my_set_4 = {1, 2, 3, 4, 5}
while my_set_4:
    item = my_set_4.pop()
    print(f"Popped item: {item}")
