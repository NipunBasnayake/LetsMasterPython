from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# Generate Rayleigh distributed data
data = random.rayleigh(scale=1000, size=1000)

sns.kdeplot(data)
plt.title("Rayleigh Distribution")
plt.xlabel("Value")
plt.ylabel("Density")
plt.show()
