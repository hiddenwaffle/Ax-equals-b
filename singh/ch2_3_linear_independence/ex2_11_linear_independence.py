import numpy as np
from util.graph import Graph
from sympy import Matrix

u = np.array([-1, 1])
v = np.array([2, 3])
# Solve Ax=0 where A = (u v)
A = np.array([u, v, [0, 0]]).T
A, _ = Matrix(A).rref()
A = np.array(A)
print(A)
# u and v are linearly independent because scalars k and c = zero

g = Graph()
g.add_vector(u, color='b')
g.add_vector(v, color='g')
g.show()
