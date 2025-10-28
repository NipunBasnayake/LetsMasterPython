import numpy as np
from scipy.optimize import minimize_scalar, differential_evolution  # correct spelling

# -----------------------------
# Example 1: Minimizing a quadratic function
# -----------------------------
def quadratic_function(x):
    # Example quadratic function: f(x) = x^2 - 4x + 3
    # a, b, c are fixed here for simplicity
    a, b, c = 1, -4, 3
    return a*x**2 + b*x + c

# minimize_scalar finds the minimum of a **univariate** function
res = minimize_scalar(quadratic_function)
print("Optimal Solution (1D):", res.x)  # x value that minimizes the function
print("Minimal Value (1D):", res.fun)   # minimum function value

# -----------------------------
# Example 2: Global optimization for multivariate function
# -----------------------------
def global_objective(x):
    # Multivariate function: f(x1, x2, ...) = sum of squares
    return np.sum(x**2)

# differential_evolution is used for **global optimization** over bounds
bounds = [(-2, 2), (-2, 2)]  # bounds for each variable x1 and x2
res_global = differential_evolution(global_objective, bounds)
print("Global Optimal Solution (multivariate):", res_global.x)
print("Global Minimal Value (multivariate):", res_global.fun)
