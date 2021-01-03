from sympy import *

a, b, c, d = symbols('a b c d')
M = Matrix([
    [a, b],
    [c, d]
])
P = Matrix([
    [0, 1],
    [1, 0]
])
# original
pprint(M)
# left multiply to exchange rows
pprint(P * M)
# right multiply to exchange columns
pprint(M * P)
