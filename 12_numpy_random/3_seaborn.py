import matplotlib.pyplot as plt
import seaborn as sns

# Option 1: Using kdeplot (for smooth density curve)
sns.kdeplot([0, 1, 2, 3, 4, 5])
plt.show()

# Option 2: Using displot (for histogram or KDE plots)
# sns.displot([0, 1, 2, 3, 4, 5], kind="kde")  # Alternate version
