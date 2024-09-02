#Q1. Write a Python program to count the occurrences of each word in a given sentence 
#string = “To change the overall look of your document. To change the look available in the gallery” 

# Given sentence
sentence = "To change the overall look of your document. To change the look available in the gallery"

# Convert the sentence to lowercase and split it into words
words = sentence.lower().split()

# Create an empty dictionary to store word counts
word_count = {}

# Loop through each word in the list of words
for word in words:
    # If the word is already in the dictionary, increment its count
    if word in word_count:
        word_count[word] += 1
    # If the word is not in the dictionary, add it with a count of 1
    else:
        word_count[word] = 1

# Print the dictionary containing word counts
print(word_count)

#ANS=> string = “To change the overall look of your document. To change the look available in the gallery” 
#ANS=> {'to': 2, 'change': 2, 'the': 3, 'overall': 1, 'look': 2, 'of': 1, 'your': 1, 'document.': 1, 'available': 1, 'in': 1, 'gallery': 1}