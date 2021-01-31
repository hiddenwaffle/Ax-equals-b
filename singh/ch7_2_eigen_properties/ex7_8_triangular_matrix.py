from sympy import *

A = Matrix([
    [5, 3, 5, 8],
    [0, 9, 7, -9],
    [0, 0, 6, -5],
    [0, 0, 0, -17]
])
pprint(A.eigenvals())  # same as the diagonal
