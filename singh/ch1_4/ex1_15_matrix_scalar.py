import numpy as np
from util.graph import Graph

A = np.array([
    [2, 2, 0],
    [0, 3, 0]
])
print(A)

g = Graph()

for v in A.T:
    g.append(v)

A *= 2
print(A)

for v in A.T:
    g.append(v, color='tab:blue')

g.show()
