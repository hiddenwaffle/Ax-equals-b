import numpy as np
from util.graph import Graph

A = np.array([
    [1, 0.2],
    [0, 1]
])
F = np.array([
    [1, 1, 2, 2, 1.4, 1.4, 2, 2, 1.4, 1.4],
    [1, 3, 3, 2.6, 2.6, 2, 2, 1.6, 1.6, 1]
])

g = Graph()
g.add_shape(F)

result = A @ F
print(result)
g.add_shape(result, color="tab:blue")

g.show()
