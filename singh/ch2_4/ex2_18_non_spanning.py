import numpy as np
from sympy import *
from util.graph import Graph

u = Matrix([1, -2])
v = Matrix([0, 0])
a, b = symbols('a b')
w = Matrix([a, b])

m = Matrix.hstack(u, v, w)
m, _ = m.rref()
pprint(m)
print('u and v are linearly dependent')

u = np.array(u, dtype=float)
v = np.array(v, dtype=float)

g = Graph()
g.add_vector(u, color='tab:blue')
g.add_vector(v, color='tab:green')
g.show()
