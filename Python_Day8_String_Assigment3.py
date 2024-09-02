#Q3. Write a Python program to reverse words in a string 
#String = “Deeptech Python Training”

# Given string
string = "Deeptech Python Training"

# Split the string into a list of words
words = string.split()

# Reverse the list of words using slicing
reversed_words = words[::-1]

# Join the reversed list of words into a single string with spaces in between
reversed_string = ' '.join(reversed_words)

# Print the reversed string
print(reversed_string)

#ANS=> String = “Deeptech Python Training”
#ANS=> Training Python Deeptech