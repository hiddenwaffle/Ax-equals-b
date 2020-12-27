from sympy import *

print('a')
m = Matrix([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0]
])
pprint(m)
print('linearly independent')

print('b')
m, _ = Matrix([
    [2, 1, 0, 0],
    [2, 2, 0, 0],
    [2, -1, 1, 0]
]).rref()
pprint(m)
print('linearly independent')

print('c')
m, _ = Matrix([
    [1, -2, 0, 0],
    [1, -2, 0, 0],
    [1, -2, 0, 0]
]).rref()
pprint(m)
print('linearly dependent')

print('d')
m, _ = Matrix([
    [-1, 0, 2, 0],
    [2, -4, 0, 0],
    [-3, 6, 6, 0]
]).rref()
pprint(m)
print('linearly independent')
