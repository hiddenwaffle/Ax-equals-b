from sympy import *

a, b, c, d, e, f, g, h, i, j, k = symbols('a b c d e f g h i j k')
A = Matrix([
    [a, b, c],
    [d, e, f],
    [g, h, i]
])
print('general matrix A:')
pprint(A)

print('a')
E = Matrix([
    [1, 0, 0],
    [0, -1, 0],
    [0, 0, 1]
])
pprint(E @ A)

print('b')
E = Matrix([
    [0, 0, 1],
    [0, 1, 0],
    [1, 0, 0]
])
pprint(E @ A)

print('c')
E = Matrix([
    [k, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
])
pprint(E @ A)

print('d')
E = Matrix([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, -1 / k]
])
pprint(E @ A)
