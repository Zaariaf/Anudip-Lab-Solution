#Q2. Write a function in Python to count and display the total number of words in a text file “ABC.txt”

def count_words_in_file():
    # Initialize a counter for the total number of words
    total_words = 0
    
    # Open the file "ABC.txt" in read mode
    with open("ABC.txt", "r") as file:
        # Iterate through each line in the file
        for line in file:
            # Split the line into words using whitespace as the delimiter
            words = line.split()
            # Add the number of words in the current line to the total count
            total_words += len(words)
    
    # Print the total number of words in the file
    print(f"Total number of words: {total_words}")

# Call the function to count and display the total number of words
count_words_in_file()

#ANS=> Total number of words: 35