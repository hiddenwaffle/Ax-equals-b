from sympy import *

A = Matrix([
    [1, 3, 4, 5],
    [2, 6, -8, -6]
])
print('finding a basis for ker(T)')
pprint(A.nullspace())
print('finding basis for range(T)')
R = A.T.rref()
pprint(R)
# Top two are non zero rows
