#Q1. Write a python program using pandas Interpolation to fill in missing values in the data frame.
#    Input: df = pd.DataFrame({"Math":[12, 4, 7, None, 2], "English":[4, 3, 57, 3, None], "Hindi":[20, 16, None, 3, 8], "Science":[14, 3, None, None, 6]})

# Import the pandas library
import pandas as pd

# Create the DataFrame with missing values
df = pd.DataFrame({
    "Math": [12, 4, 7, None, 2],
    "English": [4, 3, 57, 3, None],
    "Hindi": [20, 16, None, 3, 8],
    "Science": [14, 3, None, None, 6]
})

# Use interpolation to fill in the missing values
df_interpolated = df.interpolate()

# Display the DataFrame with interpolated values
print(df_interpolated)

#ANS=>    Math  English  Hindi  Science
#ANS=> 0  12.0      4.0   20.0     14.0
#ANS=> 1   4.0      3.0   16.0      3.0
#ANS=> 2   7.0     57.0    9.5      4.0
#ANS=> 3   4.5      3.0    3.0      5.0
#ANS=> 4   2.0      3.0    8.0      6.0