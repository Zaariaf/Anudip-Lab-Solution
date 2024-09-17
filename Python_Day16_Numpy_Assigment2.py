#Q2.  Convert the below list into a numpy array then display the array then display the first and last index and then multiply each element by 2 and display the result.
#     Input: my_list = [1, 2, 3, 4, 5]

import numpy as np  # Import the NumPy library

my_list = [1, 2, 3, 4, 5]  # Define the list
my_array = np.array(my_list)  # Convert the list to a NumPy array

print("The NumPy Array is:", my_array)  # Display the NumPy array

first_element = my_array[0]  # Get the first element of the array
last_element = my_array[-1]  # Get the last element of the array

print("The First Element is:", first_element)  # Display the first element
print("The Last Element is:", last_element)  # Display the last element

multiplied_array = my_array * 2  # Multiply each element by 2
print("The Multiplied Array is:", multiplied_array)  # Display the result

#ANS=> Input: my_list = [1, 2, 3, 4, 5]
#ANS=> The NumPy Array is: [1 2 3 4 5]
#ANS=>The First Element is: 1
#ANS=>The Last Element is: 5
#ANS=>The Multiplied Array is: [ 2  4  6  8 10]