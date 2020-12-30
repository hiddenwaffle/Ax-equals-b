from sympy import *

print('a')
A = Matrix([
    [1, 1, -1],
    [2, -1, 0],
    [5, 2, -3]
])
u = Matrix([1, 2, 3])
pprint((A * u).T)

print('b')
B = Matrix([
    [1, 4, -5],
    [-7, 5, 2]
])
u = Matrix([1, 1, 1])
pprint((B * u).T)

print('c')
C = Matrix([
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])
u = Matrix([2, 1, 5])
# pprint((C * u).T)  # Matrix size mismatch: (2, 4) * (3, 1).

print('d')
D = Matrix([
    [1, -2, 6, 1],
    [3, -6, 7, 8],
    [5, 2, 1, 7],
    [1, 6, 3, 2]
])
u = Matrix([1, 3, -4, 7])
pprint((D * u).T)
