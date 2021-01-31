from sympy import *

A = Matrix([
    [1, 4, 5, 3],
    [5, 22, 27, 11],
    [6, 19, 27, 31],
    [5, 28, 35, -8]
])
L, U, _ = A.LUdecomposition()
pprint([L, U])
pprint(L * U)
