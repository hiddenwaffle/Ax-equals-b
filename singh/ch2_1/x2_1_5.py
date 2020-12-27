import numpy as np
from util.graph import Graph

u = np.array([-3, 2])
v = np.array([-2, -3])

g = Graph()
g.add_vector(u)
g.add_vector(v)
g.show()
