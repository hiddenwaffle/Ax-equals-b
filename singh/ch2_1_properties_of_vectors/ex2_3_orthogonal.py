from sympy import *

a, b = symbols('a b')
u = Matrix([
    [a],
    [b]
])
v = Matrix([
    [b],
    [-a]
])
pprint(u.T @ v)
# 0 means orthogonal
