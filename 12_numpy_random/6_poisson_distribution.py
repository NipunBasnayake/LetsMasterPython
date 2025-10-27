from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# Generate data
normal_data = random.normal(loc=50, scale=7, size=1000)
poisson_data = random.poisson(lam=50, size=1000)

# Plot Normal distribution using kdeplot
sns.kdeplot(normal_data, label="Normal", fill=True)

# Plot Poisson distribution using kdeplot
sns.kdeplot(poisson_data, label="Poisson", fill=True)

plt.title("Normal vs Poisson Distribution")
plt.xlabel("Value")
plt.ylabel("Density")
plt.legend()
plt.show()
