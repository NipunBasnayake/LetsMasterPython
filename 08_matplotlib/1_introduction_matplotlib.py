# 1. Importing the matplotlib library
# matplotlib is a Python library used for data visualization (graphs & charts)
import matplotlib.pyplot as plt

# 2. Data for plotting
x = [1, 2, 3, 4, 5]
y = [10, 15, 25, 30, 20]

# 3. Basic line plot
plt.plot(x, y)
plt.show()

# 4. Customized line plot with markers, color, and labels
plt.plot(x, y, marker='o', linestyle='--', color='green', label='My line')

# 5. Adding axis labels and title
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('My first graph')

# 6. Displaying legend
plt.legend()

# 7. Showing the final graph
plt.show()
