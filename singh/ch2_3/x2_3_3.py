from sympy import *

print('a')
m, _ = Matrix([
    [0, -1, 0, 3],
    [1, 0, 5, 0],
    [2, 1, 0, 0],
    [0, 1, 0, -4],
    [0, 0, 0, 0]
]).T.rref()
pprint(m)
print('linearly independent')

print('b')
m, _ = Matrix([
    [1, -1, 3, 3],
    [0, 1, 5, 0],
    [-3, -6, -9, -4],
    [-5, 5, -15, -15]
]).T.rref()
pprint(m)
print('linearly dependent')

print('c')
m, _ = Matrix([
    [-2, 2, 3, 4],
    [0, 3, -2, -3],
    [2, -2, -1, 0],
    [0, 3, 0, 1]
]).T.rref()
pprint(m)
print('linearly dependent')
