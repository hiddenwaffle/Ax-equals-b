from sympy import *

print('a')
m = Matrix([
    [1, 0, 0],
    [0, 1, 0]
])
m, _ = m.rref()
pprint(m)
# k1 * column1 + k2 * column2 = 0
# k1 and k3 would have to be zero
print('linearly independent')

print('b')
m = Matrix([
    [3, -6, 0],
    [4, -8, 0]
])
m, _ = m.rref()
pprint(m)
print('linearly dependent')

print('c')
m, _ = Matrix([
    [6, -3, 0],
    [10, -5, 0]
]).rref()
pprint(m)
print('linearly dependent')

print('d')
m, _ = Matrix([
    [pi, -1, 0],
    [-2 * pi, 2, 0]
]).rref()
pprint(m)
print('linearly dependent')

print('e')
m, _ = Matrix([
    [0, -1],
    [0, 1]
]).rref()
pprint(m)
print('linearly dependent')
