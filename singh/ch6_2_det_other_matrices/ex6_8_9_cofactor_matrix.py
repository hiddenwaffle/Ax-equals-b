from sympy import *

A = Matrix([
    [1, -1, 5],
    [3, 9, 7],
    [-2, 1, 0]
])
pprint(A.cofactorMatrix())
pprint(A.cofactorMatrix().T)
# TODO: Why is it different from A.adjoint() ?
