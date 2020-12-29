import numpy as np
from util.graph import Graph

u = np.array([7, -2])
v = np.array([-5, 3])

print('a', np.linalg.norm(u + v))
print('b', np.linalg.norm(u - v))

g = Graph()
g.add_vector(u, color='r')
g.add_vector(v, color='g')
g.add_vector(u + v, color='b')
g.add_vector(u - v, color='y')
g.show()
