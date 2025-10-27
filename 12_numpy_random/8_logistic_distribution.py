from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# Generate data
normal_data = random.normal(scale=2, size=1000)
logistic_data = random.logistic(size=1000)

# Plot both distributions on the same axes
sns.histplot(normal_data, kde=True, color="blue", label="Normal", stat="density", alpha=0.5)
sns.kdeplot(logistic_data, color="red", label="Logistic")

# Add legend and title
plt.legend()
plt.title("Normal vs Logistic Distribution")
plt.show()
