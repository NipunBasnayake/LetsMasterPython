# 1. Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# 2. Data for pie chart
y = np.array([35, 25, 25, 15, 33, 21])        # Sizes of each slice
labels = ['A', 'B', 'C', 'D', 'E', 'F']      # Labels for each slice

# 3. Basic pie chart with percentage display
plt.pie(
    y,
    labels=labels,           # Slice labels
    startangle=90,           # Rotate the chart so first slice starts at 90 degrees
    autopct='%1.2f%%'        # Display percentage on slices
)
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))  # Show legend outside the chart
plt.title('Basic Pie Chart')
plt.show()

# 4. Pie chart with customized colors
colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple']
plt.pie(
    y,
    labels=labels,
    colors=colors,
    startangle=90,
    autopct='%1.1f%%'
)
plt.title('Pie Chart with Custom Colors')
plt.show()

# 5. Pie chart with exploded slices and shadow
explode = [0.1, 0, 0, 0, 0.1, 0]  # Explode first and fifth slices
plt.pie(
    y,
    labels=labels,
    colors=colors,
    explode=explode,
    startangle=90,
    shadow=True,
    autopct='%1.1f%%'
)
plt.title('Exploded Pie Chart with Shadow')
plt.show()

# 6. Pie chart with clockwise direction
plt.pie(
    y,
    labels=labels,
    colors=colors,
    startangle=90,
    counterclock=False,  # Draw slices clockwise
    autopct='%1.1f%%'
)
plt.title('Clockwise Pie Chart')
plt.show()
