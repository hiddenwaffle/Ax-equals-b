from sympy import *

A = Matrix([
    [1, 5, 3],
    [2, 3, 1],
    [3, 4, 1]
])
Ai = A.inv()
pprint(Ai)
