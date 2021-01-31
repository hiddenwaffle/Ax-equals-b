from sympy import *

A = Matrix([
    [4, -2],
    [1, 1]
])
u = Matrix([[2, 1]]).T
pprint(A * u)
pprint(3 * u)
