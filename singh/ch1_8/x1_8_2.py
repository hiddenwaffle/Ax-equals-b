from sympy import *

print('a')
m = Matrix([
    [-1, 0],
    [0, 1]
])
pprint(m.inv())

print('b')
m = Matrix([
    [0, 1],
    [1, 0]
])
pprint(m.inv())

print('c')
m = Matrix([
    [1, 0],
    [0, -2]
])
pprint(m.inv())

print('d')
m = Matrix([
    [-5, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
])
pprint(m.inv())

print('e')
m = Matrix([
    [1, 0, 0],
    [0, -sqrt(2), 0],
    [0, 0, 1]
])
pprint(m.inv())

print('f')
m = Matrix([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, pi]
])
pprint(m.inv())
