from sympy import *

print('a')
A = Matrix([
    [1, 0, 0],
    [0, 2, 0],
    [0, 0, 3]
])
Q = Matrix([GramSchmidt([A.col(0), A.col(1), A.col(2)])])
pprint(Q.T * Q)
# Not I, so not orthogonal

print('b')
B = (1 / 2) * Matrix([
    [1, 1],
    [1, 1],
    [1, -1],
    [1, -1]
])
Q = Matrix([GramSchmidt([B.col(0), B.col(1)])])
pprint(Q.T * Q)
# Not I, so not orthogonal

print('c')
C = Matrix([
    [(1 / sqrt(2)), (1 / sqrt(3)), (1 / sqrt(6))],
    [-(1 / sqrt(2)), (1 / sqrt(3)), (1 / sqrt(6))],
    [0, (1 / sqrt(3)), -(2 / sqrt(6))],
])
Q = Matrix([GramSchmidt([C.col(0), C.col(1), C.col(2)], True)])
pprint(Q.T * Q)
# I, so orthogonal
