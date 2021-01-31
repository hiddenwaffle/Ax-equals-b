from sympy import *

A = Matrix([
    [1, 1],
    [-2, 4]
])

print('a')
u = Matrix([[1, 1]]).T
pprint([A * u, 2 * u])

print('b')
v = Matrix([[1, 2]]).T
pprint([A * v, 3 * v])
