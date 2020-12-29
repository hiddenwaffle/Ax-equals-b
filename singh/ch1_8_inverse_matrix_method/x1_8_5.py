from sympy import *

print('a')
m = Matrix([
    [1, 2],
    [-1, 4]
])
b = Matrix([[3, 5]]).T
pprint(m.inv() @ b)

print('b')
m = Matrix([
    [2, -5],
    [-6, 1]
])
b = Matrix([[3, -1]]).T
pprint(m.inv() @ b)

print('c')
m = Matrix([
    [1, 0, 2],
    [2, 3, 1],
    [3, 6, 0]
])
b = Matrix([[1, 9]]).T
# pprint(m.inv() @ b)  # Matrix det == 0; not invertible.

print('d')
m = Matrix([
    [1, -1, 1],
    [1, 0, -1],
    [0, 0, -1]
])
b = Matrix([[10, 3, 5]]).T
pprint(m.inv() @ b)

print('e')
m = Matrix([
    [2, -1, 0],
    [-1, 2, -1],
    [0, -1, 2]
])
b = Matrix([[5, 7, 3]]).T
pprint(m.inv() @ b)

print('f')
m = Matrix([
    [1, 3, 4],
    [-1, 1, 1],
    [2, 1, -2]
])
b = Matrix([[-2, 3, 6]]).T
pprint(m.inv() @ b)

print('g')
m = Matrix([
    [1, 2, -2, 3],
    [-2, 1, -5, -6],
    [-5, -10, 9, -15],
    [-6, -12, 12, -19]
])
b = Matrix([[8, 1, -1, 5]]).T
pprint(m.inv() @ b)
