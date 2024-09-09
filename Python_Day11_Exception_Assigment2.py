#Q2. Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.

# Define a function to prompt the user for an integer input
def get_integer_input():
    try:
        # Prompt the user to enter an integer
        user_input = input("Please enter an integer: ")
        # Try to convert the input to an integer
        user_input = int(user_input)
    except ValueError:
        # Raise a ValueError if the input is not a valid integer
        raise ValueError("Invalid input: Please enter a valid integer.")
    else:
        # Return the valid integer input
        return user_input

# Example usage
try:
    user_number = get_integer_input()
    print(f"You entered: {user_number}")
except ValueError as e:
    # Print the error message if a ValueError is raised
    print(e)

#ANS=> Please enter an integer: 25
#ANS=>You entered: 25

#ANS=> Please enter an integer: Hello
#ANS=>Invalid input: Please enter a valid integer.