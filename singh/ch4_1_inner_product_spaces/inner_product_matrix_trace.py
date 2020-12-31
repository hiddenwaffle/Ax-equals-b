from sympy import *

# Definiting the inner product to be:
# <X, Y> = tr(Y.T @ X)

A = Matrix([
    [1, 2],
    [3, 4]
])
pprint(sqrt((A.T @ A).trace()))

B = Matrix([
    [10, 20],
    [30, 40]
])
pprint(sqrt((B.T @ B).trace()))

# notice that the norm of B is 10x A
# and that the entries of B are 10x A's entries
# coincidence? i think not
