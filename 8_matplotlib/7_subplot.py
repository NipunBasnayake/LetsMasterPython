# 1. Importing matplotlib
import matplotlib.pyplot as plt

# 2. First subplot: basic line plot
plt.subplot(2, 2, 1)  # 2 rows, 2 columns, first subplot
plt.plot([1, 2, 3], [4, 5, 6], marker='o', color='green')
plt.title('Plot 1')

# 3. Second subplot: reversed data
plt.subplot(2, 2, 2)  # 2 rows, 2 columns, second subplot
plt.plot([3, 2, 1], [6, 5, 4], marker='s', color='orange')
plt.title('Plot 2')

# 4. Third subplot: red line with square markers
plt.subplot(2, 2, 3)  # 2 rows, 2 columns, third subplot
plt.plot([1, 2, 3], [4, 5, 6], color='red', linestyle='--', marker='^')
plt.title('Red Plot')

# 5. Fourth subplot: blue line with circle markers
plt.subplot(2, 2, 4)  # 2 rows, 2 columns, fourth subplot
plt.plot([3, 2, 1], [6, 5, 4], color='blue', linestyle='-.', marker='o')
plt.title('Blue Plot')

# 6. Adjust layout to prevent overlapping titles
plt.tight_layout()

# 7. Display all subplots
plt.show()
