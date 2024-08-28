#Q3 Using max() and min() functions display the maximum and minimum of 5 random numbers.

import random

# Generate a list of 5 random numbers between 1 and 100
random_numbers = [random.randint(1, 100) for _ in range(5)]

# Find the maximum number in the list
max_number = max(random_numbers)

# Find the minimum number in the list
min_number = min(random_numbers)

# Print the list of random numbers
print("Random numbers are :", random_numbers)

# Print the maximum number
print("Maximum number is :", max_number)

# Print the minimum number
print("Minimum number is :", min_number)

#ANS=> Random numbers are : [98, 54, 3, 99, 52]
#ANS=> Maximum number is : 99
#ANS=> Minimum number is : 3
