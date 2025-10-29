file_path = "2_create_files.py"
new_file = open(file_path, "w")

new_file.write("# This is a new Python file created using the open() function 1.\n")

new_file.close()

with open(file_path, "w") as file:
    new_file.write("# This is a new Python file created using the open() function 2.\n")


file_path = "exsisisting_file.txt"

with open(file_path, "a") as file:
    exsisting_file.write("This line is appended to the existing file.\n")