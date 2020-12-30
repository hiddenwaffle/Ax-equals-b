from sympy import *

print('a')
M = Matrix([
    [2, 5, 7, 10, 3],
    [1, 1, 2, 5, 6]
])
R, _ = M.rref()
# pprint(R)
#  x  y  z  w
# ⎡1  0  1  5 | 9 ⎤
# ⎢               ⎥
# ⎣0  1  1  0 | -3⎦
# x + z + 5w = 9    => x = 9 - s - 5t
# y + z = -3        => y = -s - 3
# z = s
# w = t
s, t = symbols('s t')
x = 9 - s - 5 * t
y = -s - 3
z = s
w = t
v = Matrix([x, y, z, w])
pprint(v)
v1 = Matrix([-1, -1, 1, 0])  # s
v2 = Matrix([5, 0, 0, 1])  # t
v3 = Matrix([9, 3, 0, 0])  # "xp" (particular solution)
pprint(MatAdd(
    MatMul(s, v1),
    MatMul(t, v2),
    v3,
    evaluate=False
))
