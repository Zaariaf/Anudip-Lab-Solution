#Q1.  Write a Pandas program to create a Pivot table and find the total sale amount region wise, manager wise, sales man wise.
#    Input:Download the file salesdata.csv From LMS 

# Import the pandas library
import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('salesdata.csv')

# Display the first few rows of the DataFrame to understand its structure
print(df.head())

# Create a pivot table to find the total sale amount region-wise, manager-wise, and salesman-wise
pivot_table = pd.pivot_table(df, 
                             values='Sale_amt',  # Column to aggregate
                             index=['Region', 'Manager', 'SalesMan'],  # Columns to group by
                             aggfunc='sum')  # Aggregation function

# Print the pivot table
print("\nPivot Table:\n", pivot_table)

#ANS=>     Region  Manager   SalesMan          Item  Units  Unit_price  Sale_amt
#ANS=> 0     East   Martha  Alexander    Television     95      1198.0  113810.0
#ANS=> 1  Central  Hermann     Shelli  Home Theater     50       500.0   25000.0
#ANS=> 2  Central  Hermann       Luis    Television     36      1198.0   43128.0
#ANS=> 3  Central  Timothy      David    Cell Phone     27       225.0    6075.0
#ANS=> 4     West  Timothy    Stephen    Television     56      1198.0   67088.0

#ANS=> Pivot Table:
                            
#ANS=> Region  Manager SalesMan   Sale_amt        
#ANS=> Central Douglas John       124016.0 
#ANS=>         Hermann Luis       206373.0 
#ANS=>                 Shelli      33698.0 
#ANS=>                 Sigal      125037.5
#ANS=>         Marth   Steven      14000.0
#ANS=>         Martha  Steven     185690.0
#ANS=>         Timothy David      140955.0
#ANS=> East    Douglas Karen       48204.0
#ANS=>         Martha  Alexander  236703.0
#ANS=>                 Diana       36100.0
#ANS=> West    Douglas Michael     66836.0
#ANS=>         Timothy Stephen     88063.0