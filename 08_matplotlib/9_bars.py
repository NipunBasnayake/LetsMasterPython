# 1. Importing matplotlib library
import matplotlib.pyplot as plt

# 2. Data for plotting
categories = ['Category A', 'Category B', 'Category C', 'Category D']  # X-axis categories
values = [30, 45, 20, 60]                                           # Heights of bars (Y-axis)

# 3. Creating a bar chart
plt.bar(
    categories,
    values,
    color=['red', 'blue', 'green', 'yellow'],  # Colors for each bar
    edgecolor='black'                           # Border color of bars
)

# 4. Adding title and axis labels
plt.title('Bar Chart')
plt.xlabel('Category')
plt.ylabel('Value')

# 5. Displaying the plot
plt.show()
