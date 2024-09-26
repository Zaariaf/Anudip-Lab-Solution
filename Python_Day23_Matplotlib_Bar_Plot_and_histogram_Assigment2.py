#Q2. Visualize the daily temperature changes over time in a city and give your conclusion
#    Input: days = list(range(1, 32)) 
#    temperature = [65, 68, 70, 72, 75, 76, 78, 80, 81, 79, 75, 72, 70, 68, 67, 69, 70, 73, 75, 76, 78, 80, 81, 82, 83, 82, 80, 78, 76, 74, 71]

# Importing the necessary library for plotting
import matplotlib.pyplot as plt

# Input data
days = list(range(1, 32))  # Days of the month
temperature = [65, 68, 70, 72, 75, 76, 78, 80, 81, 79, 75, 72, 70, 68, 67, 69, 70, 73, 75, 76, 78, 80, 81, 82, 83, 82, 80, 78, 76, 74, 71]

# Creating the line chart
plt.figure(figsize=(12, 6))  # Setting the figure size
plt.plot(days, temperature, marker='o', linestyle='-', color='b')  # Plotting the line chart with markers

# Adding title and labels
plt.title('Daily Temperature Changes Over Time')  # Title of the chart
plt.xlabel('Days')  # Label for the x-axis
plt.ylabel('Temperature (°F)')  # Label for the y-axis

# Displaying the chart
plt.grid(True)  # Adding a grid for better readability
plt.show()  # Showing the plot

# Conclusion: The temperature generally increases over the month, with some fluctuations. The highest temperature is observed around the end of the month.
