from numpy import random

# Randomly select numbers from the list [5, 6, 9, 8]
# 'p' defines the probability for each element
# 'size=(100)' means it will pick 100 random elements
x = random.choice([5, 6, 9, 8], p=[0.5, 0.3, 0.2, 0.0], size=(100))

print(x)
