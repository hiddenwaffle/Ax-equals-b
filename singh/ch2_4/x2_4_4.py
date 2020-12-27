from sympy import *

print('a')
u = Matrix([1, 2])
v = Matrix([0, 1])
w = Matrix([1, 0])
m = Matrix.hstack(u, v, w, zeros(2, 1))
m, _ = m.rref()
pprint(m)
print('does not form a basis because u, v, and w are linearly dependent')

print('b')
# u = Matrix([1, 1, 1])
# v = Matrix([1, 1, 0])
# w = Matrix([0, 0, 0])
print('does not form a basis because w is all zeros')

print('c')
# u = Matrix([1, 1, 1, 1])
# v = Matrix([1, 1, 0, -1])
# w = Matrix([-1, -2, -3, 4])
# x = Matrix([2, 2, 2, 2])
print('does not form a basis because x is a scalar multiple of u')

print('d')
print('does not form a basis because there are 4 vectors in R5, and 4 is less than 5')
