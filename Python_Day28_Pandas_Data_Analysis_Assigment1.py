#Q1. Write a Pandas program to split the following data frame into groups based on Class and count the number of students in that particular class.Also generate a bar chart based on the result and explain the conclusion.
#    Input: student_data = pd.DataFrame({
#    'school_code': ['s001','s002','s003','s001','s002','s004'], 
#    'class': ['V', 'VI', 'VI', 'VI', 'V', 'VI'], 
#    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
#    'age': [12, 12, 13, 13, 14, 12], 'height': [173, 192, 186, 167, 151, 159], 
#    'weight': [35, 32, 33, 30, 31, 32],
#    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']}, )

# Import the necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Create the DataFrame with the provided data
student_data = pd.DataFrame({
    'school_code': ['s001', 's002', 's003', 's001', 's002', 's004'],
    'class': ['V', 'VI', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'age': [12, 12, 13, 13, 14, 12],
    'height': [173, 192, 186, 167, 151, 159],
    'weight': [35, 32, 33, 30, 31, 32],
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']
})

# Group the data by 'class' and count the number of students in each class
class_counts = student_data['class'].value_counts()

# Print the count of students in each class
print("Count of students in each class:\n", class_counts)

# Plot the results as a bar chart
class_counts.plot(kind='bar')

# Add title and labels to the plot
plt.title("Number of Students in Each Class")
plt.xlabel("Class")
plt.ylabel("Number of Students")

# Display the plot
plt.show()

# Conclusion: The bar chart shows that class VI has more students than class V in this dataset.

#ANS=> Count of students in each class:
#ANS=>  class
#ANS=> VI    4
#ANS=> V     2
#ANS=> Name: count, dtype: int64