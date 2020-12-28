from sympy import *

v1 = Matrix([1, -1, -1])
v2 = Matrix([6, 3, -3])
v3 = Matrix([1, 5, 1])
u = Matrix([3, 2, 1])
m = Matrix.hstack(v1, v2, v3, u)
m, _ = m.rref()
pprint(m)
# bottom row attempts to say 0 = 1, which is inconsistent, so no solution
