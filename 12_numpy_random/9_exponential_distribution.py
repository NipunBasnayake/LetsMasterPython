from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# Generate 1000 random numbers from exponential distribution
data = random.exponential(size=1000)

# Plot histogram + KDE curve
sns.histplot(data, kde=True)

plt.show()
