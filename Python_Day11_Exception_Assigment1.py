#Q1. Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.

# Define a function to perform division
def divide_numbers(a, b):
    try:
        # Try to divide the two numbers
        result = a / b
    except ZeroDivisionError:
        # Handle the case where division by zero is attempted
        return "Error: Division by zero is not allowed."
    else:
        # Return the result if no exception occurs
        return result

# Example usage
num1 = 10
num2 = 0
print(divide_numbers(num1, num2))  # This will print the error message

#ANS=> Error: Division by zero is not allowed.