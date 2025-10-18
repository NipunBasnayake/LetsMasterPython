# 1. Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# 2. Example data
data = [2, 3, 3, 4, 4, 4, 5, 5, 6, 6, 6, 6, 7, 7, 8]    # Small dataset
exam_marks = [65, 75, 56, 86, 74, 37, 86, 92, 74]       # Exam marks dataset
x = np.random.normal(170, 10, 250)                            # Random normal distribution

# 3. Basic histogram of 'data'
plt.hist(data, bins=5, color='purple', edgecolor='black')
plt.title('Histogram of Data')
plt.xlabel('Value')
plt.ylabel('Count')
plt.show()

# 4. Histogram of random normal data
plt.hist(x, bins=10, color='red', edgecolor='black')
plt.title('Histogram of Random Normal Data')
plt.xlabel('Value')
plt.ylabel('Count')
plt.show()

# 5. Histogram of exam marks
plt.hist(exam_marks, bins=5, color='red', edgecolor='black')
plt.title('Histogram of Exam Marks')
plt.xlabel('Marks')
plt.ylabel('Count')
plt.show()

# 6. Scatter over histogram (advanced exploration)
# Plot histogram
plt.hist(exam_marks, bins=5, color='lightblue', edgecolor='black', alpha=0.7)
# Scatter points for individual exam marks
plt.scatter(exam_marks, [0.5]*len(exam_marks), color='red', marker='o', label='Marks')
plt.title('Histogram with Scatter Overlay')
plt.xlabel('Marks')
plt.ylabel('Count')
plt.legend()
plt.show()
