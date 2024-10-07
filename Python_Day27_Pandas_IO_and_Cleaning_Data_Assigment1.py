#Q1. Write a Pandas program to detect missing values of a given DataFrame. 
#    Input: df = pd.DataFrame({ 'ord_no':[70001,np.nan,70002,70004,np.nan,70005,np.nan,70010,70003,70012,np.na n,70013], 'purch_amt':[150.5,270.65,65.26,110.5,948.5,2400.6,5760,1983.43,2480.4,250.45, 75.29,3045.6],
#    'ord_date': ['2012-10-05','2012-09-10',np.nan,'2012-08-17','2012-09-10','2012-07-27','2012-09-10' ,'2012-10-10','2012-10-10','2012-06-27','2012-08-17','2012-04-25'], 
#    'customer_id':[3002,3001,3001,3003,3002,3001,3001,3004,3003,3002,3001,3001],
#    'salesman_id':[5002,5003,5001,np.nan,5002,5001,5001,np.nan,5003,5002,5003,np.n an]})

# Import the pandas library
import pandas as pd
import numpy as np

# Create the DataFrame with missing values
df = pd.DataFrame({
    'ord_no': [70001, np.nan, 70002, 70004, np.nan, 70005, np.nan, 70010, 70003, 70012, np.nan, 70013],
    'purch_amt': [150.5, 270.65, 65.26, 110.5, 948.5, 2400.6, 5760, 1983.43, 2480.4, 250.45, 75.29, 3045.6],
    'ord_date': ['2012-10-05', '2012-09-10', np.nan, '2012-08-17', '2012-09-10', '2012-07-27', '2012-09-10', '2012-10-10', '2012-10-10', '2012-06-27', '2012-08-17', '2012-04-25'],
    'customer_id': [3002, 3001, 3001, 3003, 3002, 3001, 3001, 3004, 3003, 3002, 3001, 3001],
    'salesman_id': [5002, 5003, 5001, np.nan, 5002, 5001, 5001, np.nan, 5003, 5002, 5003, np.nan]
})

# Display the DataFrame
print("Original DataFrame:\n", df)

# Detect missing values
# This will return a DataFrame of the same shape with boolean values indicating missing values
missing_values = df.isnull()

# Display the DataFrame with missing values indicated
print("\nMissing values in DataFrame:\n", missing_values)

#ANS=> Missing values in DataFrame:
#ANS=>      ord_no  purch_amt  ord_date  customer_id  salesman_id
#ANS=> 0    False      False     False        False        False
#ANS=> 1     True      False     False        False        False
#ANS=> 2    False      False      True        False        False
#ANS=> 3    False      False     False        False         True
#ANS=> 4     True      False     False        False        False
#ANS=> 5    False      False     False        False        False
#ANS=> 6     True      False     False        False        False
#ANS=> 7    False      False     False        False         True
#ANS=> 8    False      False     False        False        False
#ANS=> 9    False      False     False        False        False
#ANS=> 10    True      False     False        False        False
#ANS=> 11   False      False     False        False         True