from sympy import *

A = Matrix([
    [5, 0, 0],
    [-9, 4, -1],
    [-6, 2, 1]
])
u = Matrix([[0, 1, 2]]).T
Au = A * u
pprint(Au)
pprint(A.eigenvals())
pprint(A.eigenvects())
