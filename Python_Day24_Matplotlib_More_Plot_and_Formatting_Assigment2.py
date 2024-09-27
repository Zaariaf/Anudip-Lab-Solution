#Q2. Suppose you're a sales manager for an e-commerce company, and you want to create a figure with subplots to compare the sales performance of different product categories over time. You have sales data for four product categories: Electronics, Clothing, Home & Garden, and Sports & Outdoors. Share your conclusion/analysis.
#    Input: months = np.arange(1, 13) 
#    electronics_sales = np.array([25000, 28000, 31000, 27000, 30000, 32000, 35000, 36000, 38000, 39000, 41000, 42000]) 
#    clothing_sales = np.array([15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000, 26000]) 
#    home_garden_sales = np.array([18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000, 26000, 27000, 28000, 29000])
#    sports_outdoors_sales = np.array([12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000])

import numpy as np
import matplotlib.pyplot as plt

# Data for the subplots
months = np.arange(1, 13)
electronics_sales = np.array([25000, 28000, 31000, 27000, 30000, 32000, 35000, 36000, 38000, 39000, 41000, 42000])
clothing_sales = np.array([15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000, 26000])
home_garden_sales = np.array([18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000, 26000, 27000, 28000, 29000])
sports_outdoors_sales = np.array([12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000])

# Create subplots
plt.figure(figsize=(12, 10))  # Set the figure size

# Subplot for Electronics sales
plt.subplot(2, 2, 1)  # 2 rows, 2 columns, 1st subplot
plt.plot(months, electronics_sales, marker='o', linestyle='-', color='b')
plt.title('Electronics Sales')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)

# Subplot for Clothing sales
plt.subplot(2, 2, 2)  # 2 rows, 2 columns, 2nd subplot
plt.plot(months, clothing_sales, marker='o', linestyle='-', color='g')
plt.title('Clothing Sales')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)

# Subplot for Home & Garden sales
plt.subplot(2, 2, 3)  # 2 rows, 2 columns, 3rd subplot
plt.plot(months, home_garden_sales, marker='o', linestyle='-', color='r')
plt.title('Home & Garden Sales')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)

# Subplot for Sports & Outdoors sales
plt.subplot(2, 2, 4)  # 2 rows, 2 columns, 4th subplot
plt.plot(months, sports_outdoors_sales, marker='o', linestyle='-', color='c')
plt.title('Sports & Outdoors Sales')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)

plt.tight_layout()  # Adjust subplots to fit into the figure area.
plt.show()  # Display the subplots
