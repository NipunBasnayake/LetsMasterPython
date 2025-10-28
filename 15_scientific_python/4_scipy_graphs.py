import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import (
    connected_components,
    dijkstra,
    floyd_warshall,
    bellman_ford,
    depth_first_order
)

# -----------------------------
# 1. Create adjacency matrix
# -----------------------------
# Negative weights will affect some algorithms (Dijkstra requires non-negative weights)
arr = np.array([
    [0, -1, 2],
    [1, 0, 0],
    [2, 0, 0]
])

# Convert dense adjacency matrix to sparse CSR format
graph = csr_matrix(arr)

# -----------------------------
# 2. Connected components
# -----------------------------
# Returns number of connected components and labels for each node
n_components, labels = connected_components(graph, directed=True, connection='strong')
print("Connected Components:", n_components)
print("Component labels:", labels)

# -----------------------------
# 3. Shortest path algorithms
# -----------------------------
# Dijkstra algorithm (works only with non-negative weights)
# return_predecessors=True returns the predecessor matrix to reconstruct paths
dist_matrix, predecessors = dijkstra(graph, return_predecessors=True, indices=0)
print("\nDijkstra distances from node 0:", dist_matrix)
print("Dijkstra predecessors:", predecessors)

# Floyd-Warshall algorithm (all-pairs shortest path, supports negative weights but no negative cycles)
dist_matrix_fw, predecessors_fw = floyd_warshall(graph, return_predecessors=True)
print("\nFloyd-Warshall distance matrix:\n", dist_matrix_fw)
print("Floyd-Warshall predecessors:\n", predecessors_fw)

# Bellman-Ford algorithm (single-source shortest path, supports negative weights)
dist_matrix_bf, predecessors_bf = bellman_ford(graph, return_predecessors=True, indices=0)
print("\nBellman-Ford distances from node 0:", dist_matrix_bf)
print("Bellman-Ford predecessors:", predecessors_bf)

# -----------------------------
# 4. Depth-first search
# -----------------------------
# depth_first_order returns a DFS traversal order and predecessors
order, predecessors_dfs = depth_first_order(graph, i_start=0, return_predecessors=True)
print("\nDFS order from node 0:", order)
print("DFS predecessors:", predecessors_dfs)
