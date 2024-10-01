#Q2. Suppose you want to track and analyze your household expenses for a month. You have recorded the expenses for various categories, such as groceries, utilities, rent, transportation, and entertainment. You can represent this expense data using a Pandas Series. 
#    Input: # Expense categories
#    categories = ['Groceries', 'Utilities', 'Rent', 'Transportation', 'Entertainment']
#    Monthly expense data (example data in USD) 
#    expenses = [500, 200, 1200, 300, 150]

import pandas as pd  # Importing the pandas library

# List of expense categories
categories = ['Groceries', 'Utilities', 'Rent', 'Transportation', 'Entertainment']

# Corresponding monthly expenses in USD
expenses = [500, 200, 1200, 300, 150]

# Creating a Pandas Series to represent the household expenses
expenses_series = pd.Series(data=expenses, index=categories)

# Displaying the Pandas Series
print(expenses_series)

#ANS=> Groceries          500
#ANS=> Utilities          200
#ANS=> Rent              1200
#ANS=> Transportation     300
#ANS=> Entertainment      150
#ANS=> dtype: int64