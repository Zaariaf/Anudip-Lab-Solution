#Q1. Suppose you have a dataset containing daily temperature readings for a city, and you want to identify days with extreme temperature conditions. Find days where the temperature either exceeded 35 degrees Celsius (hot day) or dropped below 5 degrees Celsius (cold day). 
#    Input: temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2,-4,-12])


import numpy as np

# Input temperature data
temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2, -4, -12])

# Identify hot days (temperature > 35 degrees Celsius)
hot_days = temperatures > 35

# Identify cold days (temperature < 5 degrees Celsius)
cold_days = temperatures < 5

# Get the indices of hot days
hot_days_indices = np.where(hot_days)[0]

# Get the indices of cold days
cold_days_indices = np.where(cold_days)[0]

# Print the indices of hot days
print("Indices of hot days:", hot_days_indices)

# Print the indices of cold days
print("Indices of cold days:", cold_days_indices)

# Print the temperatures on hot days
print("Temperatures on hot days:", temperatures[hot_days])

# Print the temperatures on cold days
print("Temperatures on cold days:", temperatures[cold_days])

#ANS=> Indices of hot days: [2 5 9]
#ANS=> Indices of cold days: [10 11]
#ANS=> Temperatures on hot days: [36.8 38.7 37.2]
#ANS=> Temperatures on cold days: [ -4. -12.]    
