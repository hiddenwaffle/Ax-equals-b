from sympy import *

M = Matrix([
    [2, -1, -4, 13],
    [3, 3, -5, 13],
    [3, -4, 10, -10]
])
R, _ = M.rref()
pprint(R)
#  x  y  z
# ⎡1  0  0  2 ⎤
# ⎢           ⎥
# ⎢0  1  0  -1⎥
# ⎢           ⎥
# ⎣0  0  1  -2⎦
# x = 2
# y = - 1
# z = -2
pprint(Matrix([2, -1, -2]))
