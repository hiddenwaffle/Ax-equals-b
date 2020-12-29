import numpy as np
from util.graph import Graph

A = np.array([
    [1, 0.5],
    [0, 1]
])
L = np.array([
    [1, 1, 1.5, 1.5, 2, 2],
    [2, 4, 4, 2.5, 2.5, 2]
])

print(L)
g = Graph()
g.add_shape(L)

L2 = A @ L
g.add_shape(L2, color='tab:blue')
print(L2)

g.show()
