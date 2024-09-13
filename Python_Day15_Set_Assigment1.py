#Q1. Write a Python program to Get Only unique items from two sets. 
#    Input: set1 = {10, 20, 30, 40, 50} set2 = {30, 40, 50, 60, 70} 

# Define the first set
set1 = {10, 20, 30, 40, 50}

# Define the second set
set2 = {30, 40, 50, 60, 70}

# Use the union operator to combine both sets and get unique items
unique_items = set1 | set2

# Print the result
print("The unique items are:",unique_items)  # Output: {70, 40, 10, 50, 20, 60, 30}

#ANS=> Input: set1 = {10, 20, 30, 40, 50} set2 = {30, 40, 50, 60, 70} 
#ANS=> The unique items are: {70, 40, 10, 50, 20, 60, 30}