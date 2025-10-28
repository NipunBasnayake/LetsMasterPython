import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

# -----------------------------
# 1. Original data points
# -----------------------------
xs = np.arange(10)        # x values: 0,1,2,...,9
ys = 2 * xs + 1           # y = 2x + 1

# -----------------------------
# 2. Create interpolation function
# -----------------------------
# kind='linear' by default; can also use 'quadratic', 'cubic'
interp_function = interp1d(xs, ys, kind='linear')

# -----------------------------
# 3. Generate interpolated values
# -----------------------------
# Interpolate at new points (can be denser than original xs)
new_xs = np.linspace(0, 9, 50)  # 50 points between 0 and 9
new_ys = interp_function(new_xs)

print("Interpolated values:\n", new_ys)

# -----------------------------
# 4. Optional: visualize interpolation
# -----------------------------
plt.scatter(xs, ys, color='red', label='Original points')
plt.plot(new_xs, new_ys, color='blue', label='Linear interpolation')
plt.xlabel('x')
plt.ylabel('y')
plt.title('1D Interpolation Example')
plt.legend()
plt.show()
