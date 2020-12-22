import numpy as np
from util.graph import Graph

u = np.array([3, -1])
v = np.array([-2, 3])
u_plus_v = u + v
print(u_plus_v)

g = Graph()
g.append(u)
g.append(v)
g.append(u_plus_v)
g.show()
