#Q3. Write a Python program to find duplicate values from a list and display those

# Initialize the list with some numbers
numbers = [1, 2, 3, 2, 4, 5, 1, 6, 3]

# Initialize an empty list to store duplicates
duplicates = []

# Iterate through each number in the list
for i in range(len(numbers)):
    # Check if the current number appears again in the list
    if numbers[i] in numbers[i+1:]:
        # Check if the number is not already in the duplicates list
        if numbers[i] not in duplicates:
            # Add the number to the duplicates list
            duplicates.append(numbers[i])

# Print the duplicate numbers
print("Duplicate values in the list:", duplicates)

#ANS=> numbers = [1, 2, 3, 2, 4, 5, 1, 6, 3]
#ANS=> Duplicate values in the list: [1, 2, 3]