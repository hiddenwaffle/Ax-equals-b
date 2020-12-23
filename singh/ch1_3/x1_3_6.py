import numpy as np
from util.graph import Graph

g = Graph()

u = np.array([-2, 2])
g.append(u, color='tab:blue')

v = np.array([2, 1])
g.append(v, color='tab:green')

left = np.array([None, None])
m = np.array([u, v])

left[0], left[1] = 1, 1
w = np.dot(left, m)
print(w)
g.append(w)

left[0], left[1] = 1/2, 1/2
w = np.dot(left, m)
print(w)
g.append(w)

left[0], left[1] = -1/2, 1/2
w = np.dot(left, m)
print(w)
g.append(w)

left[0], left[1] = 1/2, -1/2
w = np.dot(left, m)
print(w)
g.append(w)

g.show()
