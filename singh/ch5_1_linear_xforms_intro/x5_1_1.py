from sympy import *

A = Matrix([
    [0, 1],
    [1, 0]
])

print('a')
u = Matrix([1, 3])
pprint(A * u)

print('b')
u = Matrix([-1, 5])
pprint(A * u)

print('c')
u = Matrix([sqrt(2), 1])
pprint(A * u)

print('d')
u = Matrix([-2, -3])
pprint(A * u)
