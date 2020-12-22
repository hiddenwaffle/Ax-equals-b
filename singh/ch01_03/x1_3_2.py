import numpy as np
from util.graph import Graph

u = np.array([1, -1])
v = np.array([2, 1])

print('e', np.dot(u, v))
print('f', np.dot(v, u))
print('g', np.dot(u, u))
print('h', np.dot(v, v))

g = Graph()
g.append(u)
g.append(v)
g.append(u + v)
g.append(u - v)
g.show()
