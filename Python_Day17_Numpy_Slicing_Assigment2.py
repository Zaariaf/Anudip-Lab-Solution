#Q2. Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.

import numpy as np  # Import the NumPy library

# Create a 3x3 matrix with values ranging from 2 to 10
matrix = np.arange(2, 11).reshape(3, 3)
print("3x3 matrix with values from 2 to 10:\n", matrix)

#ANS=> [[ 2  3  4]
#ANS=>  [ 5  6  7] 
#ANS=>  [ 8  9 10]]