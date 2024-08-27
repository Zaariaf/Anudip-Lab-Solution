#Q3 Write a Python program that determines if a given year is a leap year or not.

# Prompt the user to enter a year
year = int(input("Enter a year: "))

# Check if the year is divisible by 4 and not divisible by 100, or divisible by 400
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    # If true, print that the year is a leap year
    print(f"{year} is a leap year.")
else:
    # If false, print that the year is not a leap year
    print(f"{year} is not a leap year.")

#Ans=> Enter a year: 2024
#ANS=> 2024 is a leap year.