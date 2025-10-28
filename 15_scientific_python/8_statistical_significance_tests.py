import numpy as np
from scipy.stats import ttest_ind

# -----------------------------
# 1. Generate two independent samples
# -----------------------------
# Sample 1: mean=0, std=1, n=100
v1 = np.random.normal(loc=0, scale=1, size=100)

# Sample 2: mean=0.5, std=1, n=100 (slightly different mean)
v2 = np.random.normal(loc=0.5, scale=1, size=100)

# -----------------------------
# 2. Perform two-sample t-test (independent)
# -----------------------------
res = ttest_ind(v1, v2)

# -----------------------------
# 3. Output
# -----------------------------
print("t-statistic:", res.statistic)
print("p-value:", res.pvalue)

# -----------------------------
# 4. Interpretation
# -----------------------------
if res.pvalue < 0.05:
    print("The difference between the samples is statistically significant (p < 0.05).")
else:
    print("No significant difference between the samples (p >= 0.05).")
