import numpy as np

# 1️⃣ Calculate sine of π/2
x1 = np.sin(np.pi / 2)
print(x1)  # 1.0

# 2️⃣ Sine of an array of angles in radians
arr = np.array([np.pi / 2, np.pi / 3, np.pi / 4, np.pi / 5])
x2 = np.sin(arr)
print(x2)  # [1.0, 0.866..., 0.707..., 0.588...]

# 3️⃣ Convert degrees to radians
array = np.array([90, 180, 270, 360])
x3 = np.deg2rad(array)
print(x3)  # [π/2, π, 3π/2, 2π]

# 4️⃣ Convert radians to degrees
array1 = np.array([np.pi / 2, np.pi, 1.5 * np.pi, 2 * np.pi])
x4 = np.rad2deg(array1)
print(x4)  # [90, 180, 270, 360]

# 5️⃣ Arcsine (inverse sine) of 1
x5 = np.arcsin(1.0)
print(x5)  # π/2 radians

# 6️⃣ Arccos (inverse cosine) of an array
array2 = np.array([1, -1, 0.1])
x6 = np.arccos(array2)
print(x6)  # [0, π, ~1.4706]

# 7️⃣ Hypotenuse using base and perpendicular
base = 3
perpendicular = 4
x7 = np.hypot(base, perpendicular)
print(x7)  # 5.0 (3-4-5 triangle)
