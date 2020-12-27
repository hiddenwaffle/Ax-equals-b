import numpy as np
from sympy import *

u = np.array([-3, 1, 0])
v = np.array([0, 1, -1])
w = np.array([2, 0, 0])

A = np.array([u, v, w, np.zeros(3)]).T
A, _ = Matrix(A).rref()
A = np.array(A, dtype=float)
print(A)
# k1 = k2 = k3 = 0, so all of the scalars are zero
# u v and w are linearly independent
