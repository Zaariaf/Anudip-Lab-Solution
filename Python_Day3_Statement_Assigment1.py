#Q1 Using input() function take one number from the user and using ternary operators check whether the number is even or odd 
# Taking input from the user
number = int(input("Enter a number: "))

# Using ternary operator to check if the number is even or odd
result = "Even" if number % 2 == 0 else "Odd"

# Printing the result
print(f"The number is {result}.")
