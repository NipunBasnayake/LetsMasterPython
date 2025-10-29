name = "Smith John"
age = 30

print("Person: " + name + ", Age: " + str(age))
print(f"Person: {name}, Age: {age}")

output = "Person: {name}, Age: {age}".format(name=name, age=age)
print(output)
