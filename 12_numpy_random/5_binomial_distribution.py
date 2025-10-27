import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random

# --- Binomial Distribution ---
n, p, size = 10, 0.5, 10000
data = np.random.binomial(n, p, size)

# Plot histogram for Binomial Distribution
plt.hist(data, bins=11, density=True, color='skyblue', edgecolor='black')
plt.title("Binomial Distribution (n=10, p=0.5)")
plt.xlabel("Number of successes")
plt.ylabel("Probability")
plt.show()

# --- Normal Distribution ---
sns.displot(
    random.normal(loc=50, scale=5, size=1000),
    kde=True,  # smoother curve
    color='salmon'
)
plt.title("Normal Distribution (mean=50, std=5)")
plt.xlabel("Value")
plt.ylabel("Density")
plt.show()
