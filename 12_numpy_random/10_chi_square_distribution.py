from numpy import random  # Import NumPy random module
import matplotlib.pyplot as plt

# Step 1: Set degrees of freedom for Chi-Square distribution
degrees_of_freedom = 3

# Step 2: Generate 1000 random values from Chi-Square distribution
data = random.chisquare(degrees_of_freedom, size=1000)

# Step 3: Plot histogram
plt.hist(data, bins=50, density=True, alpha=0.7, color='skyblue')
plt.title("Chi-Square Distribution (df = 3)")
plt.xlabel("Value")
plt.ylabel("Probability Density")
plt.show()
