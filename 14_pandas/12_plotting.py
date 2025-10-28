import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Scatter Plot to show relationship
# -----------------------------
data_relationship = {
    'X': [1, 2, 3, 4, 5],
    'Y': [5, 7, 9, 11, 13]  # Y increases linearly with X
}

# Create DataFrame
df_relationship = pd.DataFrame(data_relationship)

# Plotting a scatter plot
# kind='scatter' -> creates a scatter plot
# color='green' -> sets the marker color
# s=100 -> size of the markers (larger for better visibility)
df_relationship.plot(x='X', y='Y', kind='scatter', color='green', s=100)

plt.xlabel('X')  # Label for X-axis
plt.ylabel('Y')  # Label for Y-axis
plt.title('Scatter Plot of X vs Y')  # Title of the plot
plt.show()

# Special things:
# 1. Scatter plots are great to **visualize correlation** between two variables.
# 2. In this case, X and Y have a perfect positive linear relationship.

# -----------------------------
# Histogram to show distribution
# -----------------------------
data_distribution = {'Values': [3, 4, 5, 6, 7, 8, 9, 32, 44, 53, 67, 34, 22]}

# Create DataFrame
df_distribution = pd.DataFrame(data_distribution)

# Plotting histogram
# kind='hist' -> creates a histogram
# bins=5 -> divides data into 5 intervals
# color='blue' -> fill color for bars
# edgecolor='red' -> color of bar borders
df_distribution['Values'].plot(kind='hist', bins=5, color='blue', edgecolor='red')

plt.xlabel('Values')  # Label for X-axis
plt.ylabel('Frequency')  # Label for Y-axis
plt.title('Distribution of Values')  # Title of the plot
plt.show()

# Special things:
# 1. Histogram visualizes **frequency distribution** of numerical data.
# 2. Choosing the number of bins affects how the data is grouped and interpreted.
# 3. Large gaps (like 32, 44, 53, 67) can highlight **outliers** in the data.
