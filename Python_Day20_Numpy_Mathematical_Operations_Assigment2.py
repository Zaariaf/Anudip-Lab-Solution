#Q2. Calculate the profit made by a company
#    Input: revenue = np.array([10000, 12000, 11000, 10500]) expenses = np.array([4000, 5000, 4500, 4800])

import numpy as np  # Import the NumPy library

# Define the revenue and expenses arrays
revenue = np.array([10000, 12000, 11000, 10500])  # Revenue array
expenses = np.array([4000, 5000, 4500, 4800])     # Expenses array

# Calculate the profit by subtracting expenses from revenue element-wise
profit = revenue - expenses

# Print the profit
print("The Profit is:", profit)

#ANS=> Input: revenue = np.array([10000, 12000, 11000, 10500]) expenses = np.array([4000, 5000, 4500, 4800])
#ANS=> The Profit is: [6000 7000 6500 5700]