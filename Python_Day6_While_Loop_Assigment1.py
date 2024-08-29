#Q1. Write a python program to check whether a number is palindrome or not?

def is_palindrome(number):

   # Checks if a given number is a palindrome.

    original_number = number  # Store the original number for comparison later
    reversed_number = 0  # Initialize a variable to store the reversed number

    while number > 0:
        digit = number % 10  # Extract the last digit of the number
        reversed_number = reversed_number * 10 + digit  # Build the reversed number
        number //= 10  # Remove the last digit from the original number

    return original_number == reversed_number  # Compare original and reversed numbers

# Example usage:
num = int(input("Enter a number: "))
if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")

#ANS=> Enter a number: 69
#ANS=> 69 is not a palindrome. 

#ANS=> Enter a number: 101
#ANS-> 101 is a palindrome.  