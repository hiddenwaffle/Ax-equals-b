import numpy as np
from sympy import *
from util.graph import Graph

a, b = symbols('a b')

print('i')
m = Matrix([
    [1, -1, a],
    [2, 1, b]
])
m, _ = m.rref()
k = m.row(0)[2]
c = m.row(1)[2]
print('k and c, respectively:')
pprint([k, c])

print('ii')
u = Matrix([1, 2]).T  # first column of the original matrix
v = Matrix([-1, 1]).T  # second column of the original matrix
# We want a vector [3 2] in terms of u and v, so we use k and c
v1 = k.subs([(a, 3), (b, 2)]) * u
v2 = c.subs([(a, 3), (b, 2)]) * v

v1 = np.array(v1, dtype=float)[0]
v2 = np.array(v2, dtype=float)[0]
vv = v1 + v2
print('v1', v1)
print('v2', v2)
print('vv', vv)

u = np.array(u, dtype=float).T
v = np.array(v, dtype=float).T

g = Graph()
g.add_vector(v1, color='tab:blue')
g.add_vector(v2, color='tab:green')
g.add_vector(vv, color='tab:red')
g.add_vector(u, color='tab:orange')
g.add_vector(v, color='tab:olive')
g.show()
