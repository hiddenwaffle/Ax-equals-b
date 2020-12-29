import numpy as np
from util.graph import Graph

g = Graph()

u = np.array([-1, 1])
g.add_vector(u, 'tab:blue')

v = np.array([3, -1])
g.add_vector(v, 'tab:green')

m = np.array([u, v])
print(m)

left = np.array([1, None])

left[1] = 1
w = np.dot(left, m)
print('a', w)
g.add_vector(w)

left[1] = -1
w = np.dot(left, m)
print('b', w)
g.add_vector(w)

left[1] = 1 / 2
w = np.dot(left, m)
print('c', w)
g.add_vector(w)

left[1] = -1 / 2
w = np.dot(left, m)
print('d', w)
g.add_vector(w)

left[1] = 1 / 3
w = np.dot(left, m)
print('e', w)
g.add_vector(w)

g.show()

