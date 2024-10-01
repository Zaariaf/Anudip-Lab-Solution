#Q1. Calculate the total revenue generated by two product categories in a store 
#    Input: category1_revenue = np.array([500, 600, 700, 550]) category2_revenue = np.array([450, 700, 800, 600]) 

import numpy as np  # Import the NumPy library

# Define the revenue arrays for two product categories
category1_revenue = np.array([500, 600, 700, 550])  # Revenue for category 1
category2_revenue = np.array([450, 700, 800, 600])  # Revenue for category 2

# Calculate the total revenue by adding the two arrays element-wise
total_revenue = category1_revenue + category2_revenue

# Print the total revenue
print("The Total Revenue is:", total_revenue)

#ANS=> Input: category1_revenue = np.array([500, 600, 700, 550]) category2_revenue = np.array([450, 700, 800, 600])
#ANS=> The Total Revenue is: [ 950 1300 1500 1150]