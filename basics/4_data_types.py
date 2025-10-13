number = 42             # Integer
floating_point = 3.14   # Float
text = "Hello, World!"  # String
boolean = True          # Boolean

print (type(number))            # <class 'int'>
print (type(floating_point))    # <class 'float'>
print (type(text))              # <class 'str'>
print (type(boolean))           # <class 'bool'>

integer_number = 10
float_number = 5.5
result = integer_number + float_number
print(result)                  # 15.5

greeting = "Hello"
name = "Alice"
full_greeting = greeting + ", " + name + "!"
print(full_greeting)           # Hello, Alice!

fruits = ["apple", "banana", "cherry"]
fruits.append("grape")
print(fruits)                  # ['apple', 'banana', 'cherry', 'grape']

cordinates = (10, 20)
print(cordinates[0])           # 10
print(cordinates[1])           # 20

is_python_fun = True
is_learning = False
print(is_python_fun)               # True
print(is_learning)                # False
print(not is_python_fun)            # False
print(is_python_fun and is_learning)  # False
print(is_python_fun or is_learning)   # True