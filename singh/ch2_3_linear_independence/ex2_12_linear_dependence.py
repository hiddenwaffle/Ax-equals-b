import numpy as np
from util.graph import Graph
from sympy import *

u = np.array([-3, 1])
v = np.array([1, -1 / 3])
# Solve Ax=0 where A = (u v)
A = np.array([u, v, [0, 0]]).T
A, _ = Matrix(A).rref()
A = np.array(A, dtype='float')
print(A)

k, c = symbols('k c')
e = k - (1 / 3) * c
print(solveset(e, c))
# FiniteSet(3.0*k)

# Show that any value of 1 results in ku + cv = the 0 vector
k = 1
c = 3.0 * k
print(k * u + c * v)  # the 0 vector

g = Graph()
g.add_vector(u, color='tab:blue')
g.add_vector(v, color='tab:green')
g.show()
