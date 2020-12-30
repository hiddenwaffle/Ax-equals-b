from sympy import *

print('b')
B = Matrix([
    [1, 3],
    [2, 5],
    [-14, -37]
])
R, _ = B.rref()
u = R.row(0).T
v = R.row(1).T
print('row space')
pprint([u, v])

R, _ = B.T.rref()
pprint(R)
u = R.row(0).T
v = R.row(1).T
print('column space')
pprint([u, v])

pprint('null space')
pprint(B.nullspace())
