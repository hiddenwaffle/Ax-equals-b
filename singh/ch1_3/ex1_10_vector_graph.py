import numpy as np
from util.graph import Graph

u = np.array([3, -1])
v = np.array([-2, 3])
u_plus_v = u + v
print(u_plus_v)

g = Graph()
g.add_vector(u)
g.add_vector(v)
g.add_vector(u_plus_v)
g.show()
