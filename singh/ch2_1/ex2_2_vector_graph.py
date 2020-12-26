import numpy as np
from util.graph import Graph

u = np.array([2, 5])
v = np.array([5, -2])
print(u @ v)
g = Graph()
g.add_vector(u, color='tab:blue')
g.add_vector(v, color='tab:green')
g.show()
