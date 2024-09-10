#Q2. Write a Python program to get the largest and smallest number from a list without builtin functions. 

# Initialize the list with some numbers
numbers = [3, 1, 4, 1, 5, 9, 2]

# Assume the first number is both the smallest and largest
smallest = numbers[0]
largest = numbers[0]

# Iterate through each number in the list
for number in numbers:
    # Check if the current number is smaller than the smallest found so far
    if number < smallest:
        smallest = number
    # Check if the current number is larger than the largest found so far
    if number > largest:
        largest = number

# Print the smallest and largest numbers
print("Smallest number in the list:", smallest)
print("Largest number in the list:", largest)

#ANS=> numbers = [3, 1, 4, 1, 5, 9, 2]
#ANS=> Smallest number in the list: 1
#ANS=> Largest number in the list: 9