#Q1. Suppose you are a teacher, and you want to analyze the exam scores of your students in a particular subject. You have recorded the scores of your students for a recent exam, and you want to represent this data using a Pandas Series.
#    Input: students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah', 'Ivy', 'Jack']
#    exam_scores = [92, 88, 76, 94, 82, 90, 85, 89, 78, 91]

import pandas as pd  # Importing the pandas library

# List of students' names
students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah', 'Ivy', 'Jack']

# Corresponding exam scores
exam_scores = [92, 88, 76, 94, 82, 90, 85, 89, 78, 91]

# Creating a Pandas Series to represent the exam scores
scores_series = pd.Series(data=exam_scores, index=students)

# Displaying the Pandas Series
print(scores_series)

#ANS=> Alice      92
#ANS=> Bob        88
#ANS=> Charlie    76
#ANS=> David      94
#ANS=> Eve        82
#ANS=> Frank      90
#ANS=> Grace      85
#ANS=> Hannah     89
#ANS=> Ivy        78
#ANS=> Jack       91
#ANS=> dtype: int64 