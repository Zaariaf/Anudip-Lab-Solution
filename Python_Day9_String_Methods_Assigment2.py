#Q2. Write a Python program to remove duplicate characters of a given string.
#Input = “String and String Function” Output: String and Function

# Input string
input_string = "String and String Function"

# Split the input string into a list of words
words = input_string.split()

# Initialize an empty list to store unique words
unique_words = []

# Iterate over each word in the list
for word in words:
    # Add the word to the unique_words list if it's not already present
    if word not in unique_words:
        unique_words.append(word)

# Join the unique words back into a single string
result = " ".join(unique_words)

# Print the result
print(result) 


#ANS=> Input = “String and String Function”
#ANS=> String and Function