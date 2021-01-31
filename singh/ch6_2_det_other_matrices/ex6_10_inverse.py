from sympy import *

A = Matrix([
    [1, -1, 5],
    [3, 9, 7],
    [-2, 1, 0]
])
Ai = A.inv()
pprint(A * Ai)
