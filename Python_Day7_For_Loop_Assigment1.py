#Q1. Python program to check if the given string is a palindrome 

# Function to check if a string is a palindrome
def is_palindrome(s):
    # Convert the string to lowercase to make the check case-insensitive
    s = s.lower()
    # Reverse the string and compare it with the original string
    return s == s[::-1]

# Input string
input_string = "RADAR"

# Check if the input string is a palindrome
if is_palindrome(input_string):
    print(f'The word "{input_string}" is a palindrome.')
else:
    print(f'The word "{input_string}" is not a palindrome.')

#ANS=> The word "RADAR" is a palindrome.
#ans=> The word "FAIR" is not a palindrome.