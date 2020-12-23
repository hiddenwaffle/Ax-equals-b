import numpy as np
from util.graph import Graph

A = np.array([
    [1, 2, 2, 1],
    [2, 2, 4, 4]
])
B = np.array([
    [4, 4, 4, 4],
    [0, 0, 0, 0]
])
C = np.array([
    [0, 1],
    [-1, 0]
])
D = np.array([
    [-1, 0],
    [0, 1]
])

g = Graph()
g.add_shape(A)
g.add_shape(A - B, color="tab:blue")
g.add_shape(3 * A, color="tab:green")
g.add_shape(C @ A, color="tab:orange")
g.add_shape(D @ A, color="tab:purple")
g.show()
