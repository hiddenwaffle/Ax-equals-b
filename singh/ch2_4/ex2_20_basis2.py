import numpy as np
from sympy import *

u = Matrix([1, 0, 1])
v = Matrix([0, 1, -1])
w = Matrix([-2, 3, 0])

m = Matrix.hstack(u, v, w, zeros(3, 1))
m, _ = m.rref()
pprint(m)
# this shows that all scalars must be 0 to get a 0 vector
print('linearly independent')
