#Q2. Write a Pandas program to create and display a DataFrame from a specified dictionary data which has the index labels. 
#    Sample Python dictionary data and list labels: 
#    exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
#    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19], 
#    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], 
#    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}

import pandas as pd  # Import the pandas library
import numpy as np  # Import the numpy library for handling NaN values

# Sample data
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
             'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
             'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
             'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}

# Create a DataFrame from the dictionary with specified index labels
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data, index=labels)

# Display the DataFrame
print(df)

#ANS=>         name  score  attempts qualify
#ANS=> a  Anastasia   12.5         1     yes
#ANS=> b       Dima    9.0         3      no
#ANS=> c  Katherine   16.5         2     yes
#ANS=> d      James    NaN         3      no
#ANS=> e      Emily    9.0         2      no
#ANS=> f    Michael   20.0         3     yes
#ANS=> g    Matthew   14.5         1     yes
#ANS=> h      Laura    NaN         1      no
#ANS=> i      Kevin    8.0         2      no
#ANS=> j      Jonas   19.0         1     yes