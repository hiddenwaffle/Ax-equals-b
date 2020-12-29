from sympy import *

M = Matrix([
    [1, -2, 2, 0.03, 1.7],
    [0, -1, 1, -0.02, -1.6],
    [1, -1, 0, -0.01, 0]
])
R, p = M.rref()
pprint(R)
print('rank', len(p))
