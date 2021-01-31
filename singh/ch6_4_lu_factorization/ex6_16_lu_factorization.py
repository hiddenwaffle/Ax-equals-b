from sympy import *

A = Matrix([
    [1, 1],
    [3, 2]
])

print('i')
L, U, _ = A.LUdecomposition()
pprint([L, U])
pprint(L * U)  # Back to original matrix
