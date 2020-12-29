from sympy import *

u = Matrix([-1, 1, -1, 1])
v = Matrix([-5, -9, -7, -1])
w = Matrix([0, 7, 1, 3])
x = Matrix([-6, -1, -7, 3])
y = Matrix([2, 5, 3, 1])
M = Matrix(5, 4, [*u, *v, *w, *x, *y])
pprint(M)
R, p = M.rref()
pprint(R)
print('rank', len(p))
