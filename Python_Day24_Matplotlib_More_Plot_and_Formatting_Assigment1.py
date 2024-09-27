#Q1. Create a pie chart to visualize the distribution of your monthly income by source. 
#    You have collected data on the various sources of your income, such as salary, freelance work, investments, and rental income. Share your conclusion/analysis.
#    Input: income_sources = ['Salary', 'Freelance', 'Investments', 'Rental', 'Other'] 
#    monthly_income = [5000, 1500, 1000, 600, 400]

import matplotlib.pyplot as plt

# Data for the pie chart
income_sources = ['Salary', 'Freelance', 'Investments', 'Rental', 'Other']
monthly_income = [5000, 1500, 1000, 600, 400]

# Create a pie chart
plt.figure(figsize=(8, 8))  # Set the figure size
plt.pie(monthly_income, labels=income_sources, autopct='%1.1f%%', startangle=140)
# autopct='%1.1f%%' displays the percentage on the pie chart
# startangle=140 starts the pie chart at a specific angle

plt.title('Monthly Income Distribution by Source')  # Title of the pie chart
plt.show()  # Display the pie chart
