import numpy as np
from sympy import *

v1 = Matrix([1, 4, -3, 6])
v2 = Matrix([9, 3, -1, -6])
v3 = Matrix([5, 2, 11, -1])
v4 = Matrix([0, 0, 0, 0])

m = Matrix.hstack(v1, v2, v3, v4, zeros(4, 1))
m, _ = m.rref()
pprint(m)
# row of zeros means there is linear dependence
