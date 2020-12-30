from sympy import *

print('c')
C = Matrix([
    [1, 3, -9, 5],
    [2, 6, 7, 1],
    [1, 3, -8, 1]
])
R, _ = C.rref()
print('row space')
u = R.row(0).T
v = R.row(1).T
w = R.row(2).T
pprint([u, v, w])

R, _ = C.T.rref()
print('column space')
u = R.row(0).T
v = R.row(1).T
w = R.row(2).T
pprint([u, v, w])
print('rank 3')

R, _ = C.rref()
# pprint(R)
#  x  y  z  w
# ⎡1  3  0  0⎤
# ⎢          ⎥
# ⎢0  0  1  0⎥
# ⎢          ⎥
# ⎣0  0  0  1⎦
# w = 0
# z = 0
# y = s
# x = -3s
s = symbols('s')
v = Matrix([-3 * s, s, 0, 0])
v = MatMul(s, v / s)
print('null space')
pprint(v)
