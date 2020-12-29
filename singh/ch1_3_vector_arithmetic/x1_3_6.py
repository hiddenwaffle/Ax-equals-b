import numpy as np
from util.graph import Graph

g = Graph()

u = np.array([-2, 2])
g.add_vector(u, color='tab:blue')

v = np.array([2, 1])
g.add_vector(v, color='tab:green')

left = np.array([None, None])
m = np.array([u, v])

left[0], left[1] = 1, 1
w = np.dot(left, m)
print(w)
g.add_vector(w)

left[0], left[1] = 1/2, 1/2
w = np.dot(left, m)
print(w)
g.add_vector(w)

left[0], left[1] = -1/2, 1/2
w = np.dot(left, m)
print(w)
g.add_vector(w)

left[0], left[1] = 1/2, -1/2
w = np.dot(left, m)
print(w)
g.add_vector(w)

g.show()
