from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# Generate 1000 random values from a normal distribution
data = random.normal(size=1000)

# Create a histogram + KDE curve
sns.displot(data, bins=20, kde=True)
plt.show()
