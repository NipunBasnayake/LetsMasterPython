import numpy as np

my_list = [1, 2, 3, 4, 5]       # Create a list

first_element = my_list[0]      # Access the first element

subste = my_list[1:4]           # Slicing from index 1 to 3

my_list[2] = 10                 # Modify the third element 

my_list.append(6)               # Append an element to the end

my_list.remove(2)               # Remove the element with value 2

print(f"my_list: {my_list}")                # Output the modified list
print(f"first_element: {first_element}")    # Output the first element
print(f"subste: {subste}")                  # Output the sliced list


my_array = np.array([1, 2, 3, 4, 5])    # Create a NumPy array
first_element_array = my_array[0]       # Access the first element

print(f"my_numpy_array: {my_array}")                      # Output the NumPy array
print(f"first_element_array: {first_element_array}")      # Output the first element of the array
