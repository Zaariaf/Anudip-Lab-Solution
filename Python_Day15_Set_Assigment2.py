#Q2. Write a Python program to Return a set of elements present in Set A or B, but not both.
#    Input: set1 = {10, 20, 30, 40, 50} set2 = {30, 40, 50, 60, 70} 

# Define the first set
set1 = {10, 20, 30, 40, 50}

# Define the second set
set2 = {30, 40, 50, 60, 70}

# Use the symmetric difference operator to get elements present in either set1 or set2, but not both
symmetric_difference = set1 ^ set2

# Print the result
print("The Symmetric Difference is:",symmetric_difference)  # Output: {20, 70, 10, 60}

#ANS=> Input: set1 = {10, 20, 30, 40, 50} set2 = {30, 40, 50, 60, 70}
#ANS=> The Symmetric Difference is: {20, 70, 10, 60}