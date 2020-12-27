import numpy as np
from util.graph import Graph

u = np.array([1, 5])
v = np.array([4, 1])

print('i')
print(np.linalg.norm(u @ v))

print('ii')
print(np.linalg.norm(u) * np.linalg.norm(v))

print('iii')
print(np.linalg.norm(u) + np.linalg.norm(v))

print('iv')
print(np.linalg.norm(u + v))

g = Graph()
g.add_vector(u)
g.add_vector(v)
g.add_vector(u + v, color='tab:blue')
g.add_vector(u, v, color='tab:green')
g.show()
