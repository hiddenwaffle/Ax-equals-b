from sympy import *

A = Matrix([
    [10, 15, 0],
    [2, 4, 0],
    [3, 6, 6]
])
pprint(A.charpoly())
pprint(A.inv())
