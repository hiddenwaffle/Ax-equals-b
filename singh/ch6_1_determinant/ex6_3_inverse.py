from sympy import *

a, b, c, d = symbols('a b c d')
A = Matrix([
    [a, b],
    [c, d]
])
B = (1 / A.det()) * Matrix([
    [d, -b],
    [-c, a]
])
pprint(simplify(A * B))
