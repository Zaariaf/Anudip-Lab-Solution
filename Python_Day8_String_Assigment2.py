#Q2. Write a Python program to remove a newline in Python
#String = "\nBest \nDeeptech \nPython \nTraining\n" 

# Given string with newline characters
string_with_newlines = "\nBest \nDeeptech \nPython \nTraining\n"

# Use the replace() method to remove newline characters '\n' and replace them with an empty string
string_without_newlines = string_with_newlines.replace('\n', '')

# Print the string without newline characters
print(string_without_newlines)

#ANS=> String = "\nBest \nDeeptech \nPython \nTraining\n" 
#ANS=> Best Deeptech Python Training