#Q2. Using SciPy Linear Algebra please solve the below problem. Input: 7x + 2y = 8 4x + 5y = 10

# Import necessary libraries
import numpy as np  # For numerical operations
from scipy.linalg import solve  # For solving linear algebra problems

# Define the coefficients of the system of equations
# 7x + 2y = 8
# 4x + 5y = 10
# The coefficients are stored in a 2x2 matrix
coefficients = np.array([[7, 2], [4, 5]])

# Define the constants on the right side of the equations
# The constants are stored in a 1D array
constants = np.array([8, 10])

# Use the solve function from scipy.linalg to find the values of x and y
solution = solve(coefficients, constants)

# Display the solution
# The result is printed, showing the values of x and y
print(f"The solution of x is = {solution[0]}")
print(f"The solution of y is = {solution[1]}")

#ANS=> The solution of x is = 0.7407407407407407
#ANS=> The solution of y is = 1.4074074074074074