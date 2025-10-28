import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample dataset containing Age, Income, and Expenses
data = {
    'Age': [25, 34, 21, 34, 56],
    'Income': [25000, 36000, 25900, 60000, 30000],
    'Expenses': [20000, 30000, 20000, 40000, 20000]
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Calculate the correlation matrix
# df.corr() computes the pairwise correlation between numerical columns
# Values range from -1 to 1:
#   1 means perfect positive correlation
#   -1 means perfect negative correlation
#   0 means no correlation
correlation_matrix = df.corr()
print("\nCorrelation matrix:")
print(correlation_matrix)

# Plotting the correlation matrix as a heatmap
# annot=True -> displays the correlation values on the heatmap
# cmap='coolwarm' -> color gradient from cool (blue) to warm (red)
# linewidths=.5 -> lines between cells for clarity
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=.5)

# Adding a title to the heatmap
plt.title('Correlation Matrix')

# Display the heatmap
plt.show()
