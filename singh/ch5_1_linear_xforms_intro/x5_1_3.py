from sympy import *

# Represent this as a matrix
# x + y
# y + z
# z + x

M = Matrix([
    [1, 1, 0],
    [0, 1, 1],
    [1, 0, 1]
])

print('a')
u = Matrix([2, 4, 7])
pprint(M * u)

print('b')
u = Matrix([-3, 8, -6])
pprint(M * u)

print('c')
u = Matrix([pi, 2 * pi, 5 * pi])
pprint(M * u)

print('d')
u = Matrix([Rational(1, 2), Rational(2, 3), Rational(3, 4)])
pprint(M * u)
