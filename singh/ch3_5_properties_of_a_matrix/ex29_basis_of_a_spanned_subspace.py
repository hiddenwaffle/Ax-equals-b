from sympy import *

u = Matrix([[1, 2, 3]]).T
v = Matrix([[4, 5, 6]]).T
w = Matrix([[7, 8, 9]]).T

A = Matrix(3, 3, [*u, *v, *w])
pprint(A)
R, p = A.rref()
pprint(R)
pprint(p)

r1 = R.row(0)
r2 = R.row(1)
print(pretty(r1), 'and', pretty(r2), ' are a basis for vector space S')
