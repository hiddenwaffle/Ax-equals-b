from sympy import *

A = Matrix([
    [1, -2, -3],
    [0, 2, 5],
    [0, 0, 2]
])
pprint(A.eigenvects())
# Two eigenvectors for eigenvalue 2 are the same, so they are linearly dependent

# pprint(A.diagonalize())  # sympy.matrices.common.MatrixError: Matrix is not diagonalizable
