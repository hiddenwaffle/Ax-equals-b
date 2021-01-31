from sympy import *

A = Matrix([
    [3, 0],
    [0, 2]
])
P = eye(2)
pprint(P.inv() * A * P)
# A is already a diagonal matrix
