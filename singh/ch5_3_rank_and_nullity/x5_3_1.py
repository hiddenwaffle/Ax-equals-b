from sympy import *

print('a')
A = Matrix([
    [1, 2],
    [1, 2]
])
pprint(A.nullspace())
pprint(A.T.rref())

print('b')
A = Matrix([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
])
pprint(A.nullspace())
pprint(A.T.rref())
