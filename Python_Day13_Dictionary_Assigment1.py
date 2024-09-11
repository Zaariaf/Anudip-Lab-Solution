#Q1. Write a Python program and calculate the mean of the below dictionary.

#test_dict = {"A" : 6, "B" : 9, "C" : 5, "D" : 7, "E" : 4} 

# Define the dictionary
test_dict = {"A": 6, "B": 9, "C": 5, "D": 7, "E": 4}

# Calculate the sum of all values in the dictionary
total_sum = sum(test_dict.values())

# Calculate the number of items in the dictionary
num_items = len(test_dict)

# Calculate the mean by dividing the total sum by the number of items
mean = total_sum / num_items

# Print the calculated mean
print("The mean is:", mean)

#ANS=> test_dict = {"A": 6, "B": 9, "C": 5, "D": 7, "E": 4}
#ANS=> The mean is: 6.2