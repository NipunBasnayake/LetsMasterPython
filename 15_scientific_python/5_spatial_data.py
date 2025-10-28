import numpy as np
from scipy.sparse import csr_matrix, csc_matrix, coo_matrix, lil_matrix, dok_matrix

# -----------------------------
# 1. Create a dense matrix
# -----------------------------
dense_matrix = np.array([[1, 0, 0], [0, 5, 6], [7, 0, 9]])
print("Dense Matrix:\n", dense_matrix)

# -----------------------------
# 2. Convert dense matrix to sparse formats
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

# Access internal data
print("\nCSR Data:", csr.data)
print("CSR Indices:", csr.indices)
print("CSR Indptr:", csr.indptr)

# Sparse + Sparse
sum_matrix = csr + csr
print("\nSum of CSR + CSR:\n", sum_matrix)

# Sparse * Dense
dense_result = csr.dot(dense_matrix)
print("\nCSR multiplied by dense matrix:\n", dense_result)

# Element-wise multiplication
elementwise = csr.multiply(csr)
print("\nElement-wise multiplication of CSR with itself:\n", elementwise)

# -----------------------------
# 4. Conversion between formats
# -----------------------------
csr_to_csc = csr.tocsc()
csc_to_coo = csc.tocoo()
lil_to_csr = lil.tocsr()

print("\nCSR converted to CSC:\n", csr_to_csc)
print("\nCSC converted to COO:\n", csc_to_coo)
print("\nLIL converted to CSR:\n", lil_to_csr)

# -----------------------------
# 5. Convert sparse back to dense
# -----------------------------
dense_from_csr = csr.toarray()
print("\nDense from CSR:\n", dense_from_csr)

# -----------------------------
# 6. Example with large sparse matrix
# -----------------------------
large_sparse = csr_matrix((1000, 1000))  # 1000x1000 sparse zero matrix
large_sparse[0, 0] = 1
large_sparse[500, 500] = 5
print("\nLarge sparse matrix sample non-zero entries:\n", large_sparse)

# -----------------------------
# 7. Sparse matrix slicing
# -----------------------------
print("\nSlice of CSR matrix (first 2 rows, first 2 columns):\n", csr[:2, :2].toarray())
