# Import required libraries
import numpy as np                  # For numerical operations
import matplotlib.pyplot as plt     # For plotting graphs
import seaborn as sns               # Optional: for styling and visualization
from numpy import random            # To generate random numbers

# Set the shape parameter (alpha) for the Pareto distribution
shape_parameter = 2.5

# Generate 1000 random values following the Pareto distribution
data = random.pareto(shape_parameter, size=1000)

# Plot a histogram of the generated data
# bins=50 → number of bars in the histogram
# density=True → normalize the histogram to form a probability density
# alpha=0.7 → transparency level
# color='skyblue' → bar color
# edgecolor='black' → outline color of the bars
plt.hist(data, bins=50, density=True, alpha=0.7, color='skyblue', edgecolor='black')

# Add a title and axis labels for clarity
plt.title("Pareto Distribution (shape = 2.5)")
plt.xlabel("Value")
plt.ylabel("Probability Density")

# Display the plot on screen
plt.show()
