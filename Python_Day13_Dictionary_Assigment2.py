#Q2. Write a Python script to concatenate the following dictionaries to create a new one. 

#Sample Dictionary : dic1={1:10, 2:20} dic2={3:30, 4:40} dic3={5:50,6:60} 

# Define the sample dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Create a new dictionary by concatenating the above dictionaries
# Using the unpacking operator (**)
result_dict = {**dic1, **dic2, **dic3}

# Print the resulting concatenated dictionary
print("The concatenated dictionary is:", result_dict)


#ANS=> dic1 = {1: 10, 2: 20}
#ANS=> dic2 = {3: 30, 4: 40}
#ANS=> dic3 = {5: 50, 6: 60}
#ANS=> The concatenated dictionary is: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}