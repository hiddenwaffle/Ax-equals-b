from sympy import *

A = Matrix([
    [1, 2],
    [2, 4]
])
B = Matrix([
    [-1, 3, 9],
    [-5, 2, 6]
])
C = Matrix([
    [-3, 6],
    [-5, 2],
    [-2, 7]
])

pprint(A.rank())
pprint(B.rank())
pprint(C.rank())
# notice that these correspond to the # of vectors in each basis as found in ex28
