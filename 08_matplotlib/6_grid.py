# 1. Importing matplotlib library
import matplotlib.pyplot as plt

# 2. Data for plotting
x = [1, 2, 3, 4, 5]
y = [10, 15, 20, 25, 30]

# 3. Create a figure with 1 row and 2 columns of subplots

# First subplot: basic line plot with default grid
plt.subplot(1, 2, 1)  # 1 row, 2 columns, first subplot
plt.plot(x, y, marker='o', color='blue', label='Linear')
plt.title("Default Grid")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.grid(True)  # Show default grid
plt.legend()

# Second subplot: squared values with customized grid
plt.subplot(1, 2, 2)  # 1 row, 2 columns, second subplot
plt.plot(x, [i**2 for i in y], marker='s', color='red', label='Squared')
plt.title("Customized Grid")
plt.xlabel("X axis")
plt.ylabel("Y^2 axis")
plt.grid(color='gray', linestyle='--', linewidth=0.7)  # Custom grid
plt.legend()

# 4. Adjust layout to prevent overlap
plt.tight_layout()

# 5. Display the figure
plt.show()

# Extra exploration:
# Try changing grid parameters like:
# color='green', linestyle='-.', linewidth=1, alpha=0.5
# See how the grid appearance changes!
