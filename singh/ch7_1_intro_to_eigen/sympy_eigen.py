from sympy import *

A = Matrix([
    [1, 0, 4],
    [0, 4, 0],
    [3, 5, -3]
])
pprint(A.eigenvals())
pprint(A.eigenvects())
