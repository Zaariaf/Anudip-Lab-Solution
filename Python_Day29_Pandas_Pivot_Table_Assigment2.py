#Q2. Write a Pandas program to create a Pivot table and find the item wise unit sold.
#    Input:Download the file salesdata.csv From LMS

# Import the pandas library
import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('salesdata.csv')

# Display the first few rows of the DataFrame to understand its structure
print(df.head())

# Create a pivot table to find the item-wise units sold
pivot_table_units = pd.pivot_table(df, 
                                   values='Units',  # Column to aggregate
                                   index=['Item'],  # Column to group by
                                   aggfunc='sum')  # Aggregation function

# Print the pivot table
print("\nItem-wise Units Sold Pivot Table:\n", pivot_table_units)

#ANS=>     Region  Manager   SalesMan          Item  Units  Unit_price  Sale_amt
#ANS=> 0     East   Martha  Alexander    Television     95      1198.0  113810.0
#ANS=> 1  Central  Hermann     Shelli  Home Theater     50       500.0   25000.0
#ANS=> 2  Central  Hermann       Luis    Television     36      1198.0   43128.0
#ANS=> 3  Central  Timothy      David    Cell Phone     27       225.0    6075.0
#ANS=> 4     West  Timothy    Stephen    Television     56      1198.0   67088.0

#ANS=> Item-wise Units Sold Pivot Table:
#ANS=>                Units
#ANS=> Item
#ANS=> Cell Phone      278
#ANS=> Desk             10
#ANS=> Home Theater    722
#ANS=> Television      716
#ANS=> Video Games     395