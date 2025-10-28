import numpy as np
from scipy.sparse import csr_matrix, csc_matrix, coo_matrix, lil_matrix, dok_matrix

# -----------------------------
# 1. Create a dense matrix
# -----------------------------
dense_matrix = np.array([[1, 0, 0], [0, 1, 2], [0, 0, 3]])
print("Dense Matrix:")
print(dense_matrix)

# -----------------------------
# 2. Convert dense to sparse formats
# -----------------------------
csr = csr_matrix(dense_matrix)  # Compressed Sparse Row
csc = csc_matrix(dense_matrix)  # Compressed Sparse Column
coo = coo_matrix(dense_matrix)  # Coordinate format
lil = lil_matrix(dense_matrix)  # List of lists format
dok = dok_matrix(dense_matrix)  # Dictionary of keys format

print("\nCSR Matrix:\n", csr)
print("\nCSC Matrix:\n", csc)
print("\nCOO Matrix:\n", coo)
print("\nLIL Matrix:\n", lil)
print("\nDOK Matrix:\n", dok)

# -----------------------------
# 3. Sparse matrix operations
# -----------------------------
# Remove explicit zeros
csr.eliminate_zeros()

# Sum duplicates (important for COO format)
coo.sum_duplicates()

# Access non-zero data and indices
print("\nCSR Data:", csr.data)
print("CSR Indices:", csr.indices)
print("CSR Indptr:", csr.indptr)

# Convert between formats
csr_to_csc = csr.tocsc()
csc_to_coo = csc.tocoo()
lil_to_csr = lil.tocsr()

print("\nCSR converted to CSC:\n", csr_to_csc)
print("\nCSC converted to COO:\n", csc_to_coo)
print("\nLIL converted to CSR:\n", lil_to_csr)

# -----------------------------
# 4. Basic operations
# -----------------------------
# Sparse + Sparse
sum_matrix = csr + csr
print("\nSum of CSR + CSR:\n", sum_matrix)

# Sparse * Dense
dense_result = csr.dot(dense_matrix)
print("\nCSR multiplied by dense matrix:\n", dense_result)

# Sparse element-wise operations (using .multiply)
elementwise = csr.multiply(csr)
print("\nElement-wise multiplication of CSR with itself:\n", elementwise)

# -----------------------------
# 5. Convert back to dense
# -----------------------------
dense_from_csr = csr.toarray()
print("\nDense from CSR:\n", dense_from_csr)
