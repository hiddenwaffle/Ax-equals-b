from sympy import *

A = Matrix([
    [1, 2, 3],
    [4, 5, 6],
    [3, -3, 5]
])
pprint(A.LUdecomposition())
