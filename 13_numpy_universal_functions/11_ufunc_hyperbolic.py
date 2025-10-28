import numpy as np

# 1️⃣ Hyperbolic sine of π/2
x = np.sinh(np.pi / 2)
print(x)  # ≈ 2.3013

# 2️⃣ Inverse hyperbolic sine of 2.0
x1 = np.arcsinh(2.0)
print(x1)  # ≈ 1.4436

# 3️⃣ Inverse hyperbolic sine of an array
array = np.array([0.1, 0.2, 0.3, 0.4, 0.5])
x2 = np.arcsinh(array)
print(x2)  # ≈ [0.0998, 0.1987, 0.2958, 0.3879, 0.4812]
