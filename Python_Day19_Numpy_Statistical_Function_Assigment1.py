#Q1. Compute the median of the flattened NumPy array 
#    Input: x_odd = np.array([1, 2, 3, 4, 5, 6, 7])

import numpy as np  # Import the NumPy library

# Create a NumPy array with the given input
x_odd = np.array([1, 2, 3, 4, 5, 6, 7])

# Compute the median of the flattened array
median_value = np.median(x_odd)

# Print the median value
print("Median of the array:", median_value)

#ANS=> Input: x_odd = np.array([1, 2, 3, 4, 5, 6, 7])
#ANS=> Median of the array: 4.0