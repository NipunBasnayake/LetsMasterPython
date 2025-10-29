# 1. Importing matplotlib
import matplotlib.pyplot as plt

# 2. Data for plotting
x = [2, 4, 6, 7, 8]
y = [10, 15, 20, 25, 30]

# 3. Creating a customized scatter plot
plt.scatter(
    x, y,
    color='red',       # Fill color of points
    s=100,             # Size of markers
    edgecolor='black', # Border color of markers
    marker='o'         # Shape of markers
)

# 4. Adding title and labels
plt.title('Customized Scatter Plot')
plt.xlabel('X axis')
plt.ylabel('Y axis')

# 5. Display the plot
plt.show()
