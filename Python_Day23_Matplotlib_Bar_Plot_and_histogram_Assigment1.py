#Q1. Create a bar chart to represent monthly expenses in different spending categories and give your conclusion. 
#    Input: categories = ['Rent', 'Groceries', 'Utilities', 'Entertainment', 'Transportation'] expenses = [1200, 400, 200, 150, 250]

# Importing the necessary library for plotting
import matplotlib.pyplot as plt

# Input data
categories = ['Rent', 'Groceries', 'Utilities', 'Entertainment', 'Transportation']
expenses = [1200, 400, 200, 150, 250]

# Creating the bar chart
plt.figure(figsize=(10, 6))  # Setting the figure size
plt.bar(categories, expenses, color='skyblue')  # Plotting the bar chart

# Adding title and labels
plt.title('Monthly Expenses by Category')  # Title of the chart
plt.xlabel('Categories')  # Label for the x-axis
plt.ylabel('Expenses in Dollars')  # Label for the y-axis

# Displaying the chart
plt.show()  # Showing the plot

# Conclusion: Rent is the highest expense, followed by Groceries. Entertainment and Utilities have the lowest expenses.
