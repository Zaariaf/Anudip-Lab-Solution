#Q2. Python program to check if a given number is an Armstrong number

# Function to check if a number is an Armstrong number
def is_armstrong_number(num):
    # Convert the number to a string to easily iterate over each digit
    num_str = str(num)
    # Calculate the number of digits (order)
    order = len(num_str)
    # Initialize the sum to 0
    sum = 0
    # Iterate over each digit in the number
    for digit in num_str:
        # Convert the digit back to an integer and raise it to the power of the order
        sum += int(digit) ** order
    # Check if the sum of the powered digits is equal to the original number
    return sum == num

# Input number
input_number = 153

# Check if the input number is an Armstrong number
if is_armstrong_number(input_number):
    print(f'The number {input_number} is an Armstrong number.')
else:
    print(f'The number {input_number} is not an Armstrong number.')

#ANS=> The number 153 is an Armstrong number
#ANS=> The number 157 is not an Armstrong number