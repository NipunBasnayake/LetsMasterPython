# 1. Importing necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# 2. Basic line plot with markers
y_points = [3, 8, 1, 10]               # Y-axis values
x_points = np.arange(len(y_points))    # X-axis values: 0, 1, 2, 3

plt.plot(x_points, y_points, marker='o')  # Line plot with circular markers
plt.title("Line plot with circular markers")
plt.show()

# 3. Plotting different marker types
x = [1, 2, 3, 4, 5]
y = [10, 15, 25, 30, 20]

plt.plot(x, y, marker='o', label='Circle')    # Circle markers
plt.plot(x, y, marker='s', label='Square')    # Square markers
plt.plot(x, y, marker='^', label='Triangle')  # Triangle markers
plt.plot(x, y, marker='*', label='Star')      # Star markers

# Adding labels, title, and legend
plt.xlabel('x')
plt.ylabel('y')
plt.title('Basic Marker Types')
plt.legend()
plt.show()
