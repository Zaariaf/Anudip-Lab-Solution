#Q1. 1. Install matplotlib  & you can use plt.plot() to create a line plot of given data
#    x = [0, 5, 9, 10, 15, 20, 25] y = [0, 1, 2, 3, 4, 5, 6]

# Import the pyplot module from matplotlib and alias it as plt
import matplotlib.pyplot as plt

# Define the data for the x-axis
x = [0, 5, 9, 10, 15, 20, 25]

# Define the data for the y-axis
y = [0, 1, 2, 3, 4, 5, 6]

# Create a line plot using the x and y data
plt.plot(x, y)

# Add a title to the plot
plt.title('Line Plot of Given Data')

# Label the x-axis
plt.xlabel('X-axis')

# Label the y-axis
plt.ylabel('Y-axis')

# Display the plot
plt.show()
