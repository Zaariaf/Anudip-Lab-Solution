#Q1. Write a Pandas program to create a dataframe from a dictionary and display it.
#    Sample data:score={'Math':[78,85,96,80,86], 'English':[84,94,89,83,86],'Hindi':[86,97,96,72,83]} 

import pandas as pd  # Import the pandas library

# Sample data
score = {'Math': [78, 85, 96, 80, 86], 
         'English': [84, 94, 89, 83, 86], 
         'Hindi': [86, 97, 96, 72, 83]}

# Create a DataFrame from the dictionary
df = pd.DataFrame(score)

# Display the DataFrame
print(df)

#ANS=>    Math  English  Hindi
#ANS=> 0    78       84     86
#ANS=> 1    85       94     97
#ANS=> 2    96       89     96
#ANS=> 3    80       83     72
#ANS=> 4    86       86     83