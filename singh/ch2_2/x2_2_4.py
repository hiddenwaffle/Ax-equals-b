from sympy import *

k = symbols('k')

print('a')
u = Matrix([-1, 5, k])
v = Matrix([-3, 2, 7])
e = u.T @ v
pprint(e[0])
print('k = ', solveset(e[0], k))

print('b')
u = Matrix([2, -1, 3])
v = Matrix([3, 1, k])
e = u.T @ v
pprint(e[0])
print('k = ', solveset(e[0], k))

print('c')
u = Matrix([0, -k, sqrt(2)])
v = Matrix([-7, 5, k])
e = u.T @ v
pprint(e[0])
print('k = ', solveset(e[0], k))
