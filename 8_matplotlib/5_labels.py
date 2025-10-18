# 1. Importing matplotlib library
import matplotlib.pyplot as plt

# 2. Data for plotting
x = [1, 2, 3, 4, 5]
y = [10, 15, 20, 25, 30]   # First line
y2 = [5, 10, 15, 20, 25]   # Second line

# 3. Plotting lines with labels
plt.plot(x, y, label='Line 1')
plt.plot(x, y2, label='Line 2')

# 4. Adding axis labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Labels Explored')

# 5. Displaying legend with customization
plt.legend(loc='upper left', fontsize=12, frameon=False)

# 6. Displaying the graph
plt.show()
