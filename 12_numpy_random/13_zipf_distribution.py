from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# Generate random numbers following a Zipf distribution
# a = 2 → shape parameter (controls skewness)
# size = (3, 4) → generates a 3x4 matrix of random values
x = random.zipf(a=2, size=(3, 4))

# Filter values less than 10
# (Zipf can produce very large numbers, so we limit for better visualization)
filtered_x = x[x < 10]

# Create a distribution plot (histogram)
# kde=False → disables the smooth line curve (Kernel Density Estimate)
sns.displot(filtered_x, kde=False)

# Display the plot
plt.show()
