# ------------- exercise 01 -------------
def reverse_string(input_string):
    return input_string[::-1]

original_string = "Python Programming"
reversed_string = reverse_string(original_string)

print(f"Original string: {original_string}")
print(f"Reversed string: {reversed_string}")

# ------------- exercise 02 -------------
def count_vowels(input_text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in input_text if char in vowels)

text = "Python Programming"
vowel_count = count_vowels(text)

print(f"Text: {text}")
print(f"Number of vowels: {vowel_count}")

