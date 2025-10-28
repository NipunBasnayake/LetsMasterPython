from scipy import constants  # Import SciPy constants module

# -----------------------------
# Fundamental physical constants
# -----------------------------
speed_of_light = constants.speed_of_light  # Speed of light in vacuum (m/s)
gravitational_constant = constants.gravitational_constant  # Newton's gravitational constant (m^3 kg^-1 s^-2)
Boltzmann_constant = constants.k  # Boltzmann constant (J/K)

print("Speed of light =", speed_of_light)
print("Gravitational constant =", gravitational_constant)
print("Boltzmann constant =", Boltzmann_constant)

# -----------------------------
# Mathematical constants
# -----------------------------
pi = constants.pi  # π (3.14159...)
euler_gamma = constants.euler_gamma  # Euler-Mascheroni constant (≈ 0.577)
golden_ratio = constants.golden_ratio  # Golden ratio (≈ 1.618)

print("PI = ", pi)
print("Euler gamma = ", euler_gamma)
print("Golden ratio = ", golden_ratio)

# -----------------------------
# Unit conversion constants
# -----------------------------
mile_to_meter = constants.mile_to_meter  # 1 mile in meters
inch_to_meter = constants.inch_to_meter  # 1 inch in meters
knots_to_mps = constants.knots_to_mps  # 1 knot in meters per second

print("Mile to meter =", mile_to_meter)
print("Inch to meter =", inch_to_meter)
print("Knots to meter =", knots_to_mps)
