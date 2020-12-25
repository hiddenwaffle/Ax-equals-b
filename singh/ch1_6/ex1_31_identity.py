import numpy as np
from util.graph import Graph

A = np.array([
    [1, 3, 1],
    [1, 1, 3]
])
g = Graph()
g.add_shape(A)
I = np.identity(2)
IA = I @ A
g.add_shape(IA, color='tab:blue')
g.show()
