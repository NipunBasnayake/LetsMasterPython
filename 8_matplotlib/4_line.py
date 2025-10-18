# 1. Importing matplotlib library
import matplotlib.pyplot as plt

# 2. Data for plotting
x = [1, 2, 3, 4, 5]          # X-axis values
y = [10, 15, 25, 30, 20]     # Y-axis values for first line
y2 = [5, 10, 15, 20, 25]     # Y-axis values for second line

# 3. Plotting multiple lines
plt.plot(x, y, label='Line 1')                                # First line
plt.plot(x, y2, linestyle='--', color='red', label='Line 2')  # Second line with dashed style

# 4. Adding labels, title, and legend
plt.xlabel('x')
plt.ylabel('y')
plt.title('Multiple lines')
plt.legend()  # Shows the labels of the lines

# 5. Displaying the graph
plt.show()
