from sympy import *

A = Matrix([
    [1, -6, 2],
    [0, 4, 25],
    [0, 0, 9]
])
pprint(A.eigenvects())
P, D = A.diagonalize()
pprint((P, D))
pprint(P * D)
pprint(A * P)
# "Matrix P does indeed diagonalize the given matrix A"
