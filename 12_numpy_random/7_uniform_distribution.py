from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# Generate uniform random data
data = random.uniform(size=1000)

# Plot only the KDE (smooth density curve)
sns.displot(data, kind="kde", fill=True)  # fill=True makes it look nicer

plt.title("Uniform Distribution - Density Plot")
plt.xlabel("Value")
plt.ylabel("Density")
plt.show()
