#Q1.  Write a Python program to Count all letters, digits, and special symbols from the given string
#Input = “P@#yn26at^&i5ve” Output: Chars = 8 Digits = 2 Symbol = 3 

# Input string
input_string = "P@#yn26at^&i5ve"

# Initialize counters for letters, digits, and symbols
chars_count = 0
digits_count = 0
symbols_count = 0

# Iterate through each character in the string
for char in input_string:
    if char.isalpha():  # Check if the character is a letter
        chars_count += 1
    elif char.isdigit():  # Check if the character is a digit
        digits_count += 1
    else:  # If it's neither a letter nor a digit, it's a symbol
        symbols_count += 1

# Print the counts
print(f"Chars = {chars_count}")  # Number of letters
print(f"Digits = {digits_count}")  # Number of digits
print(f"Symbols = {symbols_count}")  # Number of symbols

#ANS=> Input = “P@#yn26at^&i5ve”
#ANS=> Chars = 8
#ANS=> Digits = 3
#ANS=> Symbols = 4