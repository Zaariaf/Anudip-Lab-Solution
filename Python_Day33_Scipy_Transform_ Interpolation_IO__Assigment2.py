#Q2. Write a python program using Interpolation to fill in missing values in the data frame. After that store the data frame into a MATLAB file using SciPy IO.
#    Then display the contents from the MATLAB file. 
#    Input: df = pd.DataFrame({"Math":[12, 4, 7, None, 2], "English":[4, 3, 57, 3, None], "Hindi":[20, 16, None, 3, 8], "Science":[14, 3, None, None, 6]})

# Import necessary libraries
import pandas as pd
from scipy.io import savemat, loadmat

# Create the DataFrame with missing values
df = pd.DataFrame({
    "Math": [12, 4, 7, None, 2],
    "English": [4, 3, 57, 3, None],
    "Hindi": [20, 16, None, 3, 8],
    "Science": [14, 3, None, None, 6]
})

# Use interpolation to fill in the missing values
df_interpolated = df.interpolate()

# Convert the DataFrame to a dictionary to save it as a MATLAB file
data_dict = {"df_interpolated": df_interpolated.to_dict(orient="list")}

# Save the DataFrame into a MATLAB file using SciPy IO
savemat("df_interpolated.mat", data_dict)

# Load the data back from the MATLAB file to verify
data_loaded = loadmat("df_interpolated.mat")

# Display the contents from the MATLAB file
print(data_loaded["df_interpolated"])

#ANS=> [[(array([[12. ,  4. ,  7. ,  4.5,  2. ]]), array([[ 4.,  3., 57.,  3.,  3.]]), array([[20. , 16. ,  9.5,  3. ,  8. ]]), array([[14.,  3.,  4.,  5.,  6.]]))]]