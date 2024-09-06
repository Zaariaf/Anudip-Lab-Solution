#Q1. Write a function in python to read the content from a text file "ABC.txt" line by line and display the same on screen.

def read_file_line_by_line():
    # Open the file "ABC.txt" in read mode
    with open("ABC.txt", "r") as file:
        # Iterate through each line in the file
        for line in file:
            # Print the current line
            print(line.strip())  # strip() removes any leading/trailing whitespace characters

# Call the function to read and display the file content
read_file_line_by_line()

#ANS=> Hello, this is a sample text file.
#ANS=>It contains multiple lines of text.       
#ANS=>Each line will be read and processed.     
#ANS=>Python is a powerful programming language.
#ANS=>This is the last line of the sample file. 