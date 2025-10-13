# ------------- example 01 -------------
text = "Python programming"

upper_case = text.upper()
lower_case = text.lower()
title_case = text.title()

print("Original text: ", text)
print("Upper case: ", upper_case)
print("Lower case: ", lower_case)
print("Title case: ", title_case)

# ------------- example 02 -------------
message = "Hello World!"

new_message = message.replace("World", "Python")
print("Original message: ", message)
print("New message: ", new_message)

# ------------- example 03 -------------
word = "python123"

is_alpha = word.isalpha()
is_numeric = word.isnumeric()

print("Original word: ", word)
print("Is alpha: ", is_alpha)
print("Is numeric: ", is_numeric)