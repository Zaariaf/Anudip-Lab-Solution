#Q4 Create a Python program that checks if a user-given number is positive, negative, or zero.

# Prompt the user to enter a number
number = float(input("Enter a number: "))

# Check if the number is greater than 0
if number > 0:
    # If true, print "Positive"
    print("The number is Positive")
# Check if the number is less than 0
elif number < 0:
    # If true, print "Negative"
    print("The number is Negative")
else:
    # If neither, print "Zero"
    print("The number is Zero")

#ANS=> Enter a number: -11
#ANS=> The number is Negative

#ANS=> Enter a number: 21
#ANS=> The number is Positive
 
#ANS=> Enter a number: 0
#ANS=> The number is Zero