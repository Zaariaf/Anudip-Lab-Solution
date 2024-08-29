#Q2. Write a python program finding the factorial of a given number using a while loop

def factorial_with_while(number):
    
    #Calculates the factorial of a given number using a while loop.
    
    result = 1  # Initialize the result to 1 (since 0! = 1)
    while number > 1:
        result *= number  # Multiply the result by the current number
        number -= 1  # Decrement the number for the next iteration
    return result  # Return the final factorial value

# Example usage:
n = int(input("Enter a number: "))
print(f"Factorial of {n} is {factorial_with_while(n)}")

#ANS=> Enter a number: 6
#ANS=> Factorial of 6 is 720