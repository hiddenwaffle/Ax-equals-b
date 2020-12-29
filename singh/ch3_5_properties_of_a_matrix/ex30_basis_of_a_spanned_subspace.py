from sympy import *

u = Matrix([[1, 3, 5, 6]]).T
v = Matrix([[1, 7, 8, 9]]).T
w = Matrix([[3, 9, 15, 18]]).T
A = Matrix(3, 4, [*u, *v, *w])
pprint(A)
R, p = A.rref()
pprint(R)
pprint(p)
r1 = R.row(0)
r2 = R.row(1)
print(pretty(r1), 'and', pretty(r2), 'are a basis for the row space')
