# 1. Importing necessary libraries
import matplotlib.pyplot as plt      # For plotting graphs
import numpy as np                   # For handling numerical data and arrays

# 2. Creating data points using NumPy arrays
x_points = np.array([1, 2, 6, 8])    # X-axis values
y_points = np.array([3, 8, 1, 10])   # Y-axis values

# 3. Plotting the data points
plt.plot(x_points, y_points)         # Draws a line connecting the points

# 4. Displaying the graph
plt.show()
