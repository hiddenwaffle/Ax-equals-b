from sympy import *

print('a')
u = Matrix([[1, 5]]).T
v = Matrix([[7, 2]]).T
M = Matrix(2, 2, [*u, *v])
R, p = M.rref()
pprint(R)
print('rank', len(p))

print('b')
u = Matrix([[-1, -3]])
v = Matrix([[4, 12]])
M = Matrix(2, 2, [*u, *v])
R, p = M.rref()
pprint(R)
print('rank', len(p))

print('c')
u = Matrix([[3, 6, 5]])
v = Matrix([[2, 1, 2]])
w = Matrix([[12, 15, 15]])
M = Matrix(3, 3, [*u, *v, *w])
R, p = M.rref()
pprint(R)
print('rank', len(p))

print('d')
u = Matrix([[-1, -2, -5]])
v = Matrix([[0, 1, 5]])
w = Matrix([[2, 3, 2]])
x = Matrix([[-4, 1, 7]])
M = Matrix(4, 3, [*u, *v, *w, *x])
R, p = M.rref()
pprint(R)
print('rank', len(p))

print('e')
u = Matrix([[1, 2, 2, 2]])
v = Matrix([[-1, 3, 5, 7]])
w = Matrix([[2, -1, -3, -5]])
x = Matrix([[0, 5, 7, 9]])
M = Matrix(4, 4, [*u, *v, *w, *x])
R, p = M.rref()
pprint(R)
print('rank', len(p))
