#Q1. Write a NumPy program to create an array of 10 zeros, 10 ones, and 10 fives

import numpy as np  # Import the NumPy library

# Create an array of 10 zeros
zeros_array = np.zeros(10)
print("Array of 10 zeros:", zeros_array)

# Create an array of 10 ones
ones_array = np.ones(10)
print("Array of 10 ones:", ones_array)

# Create an array of 10 fives
fives_array = np.full(10, 5)
print("Array of 10 fives:", fives_array)

#ANS=> Array of 10 zeros: [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
#ANS=> Array of 10 ones: [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.] 
#ANS=> Array of 10 fives: [5 5 5 5 5 5 5 5 5 5]