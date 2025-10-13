# 1. Sorting fruits alphabetically
fruit_list = ["mango", "apple", "cherry", "banana"]
fruit_list.sort()
print(fruit_list)

# 2. Sorting numbers in ascending order
numbers_list_1 = [10, 5, 20, 15, 25]
numbers_list_1.sort()
print(numbers_list_1)

# 3. Sorting numbers in descending order
numbers_list_2 = [10, 5, 20, 15, 25]
numbers_list_2.sort(reverse=True)
print(numbers_list_2)

# 4. Sorting numbers by custom key (distance from 50)
def myfunction(n):
    return abs(n - 50)

numbers_list_3 = [100, 50, 65, 82, 23]
numbers_list_3.sort(key=myfunction)
print(numbers_list_3)
