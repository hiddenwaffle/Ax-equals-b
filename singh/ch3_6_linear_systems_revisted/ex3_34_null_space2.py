from sympy import *

B = Matrix([
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])
R, p = B.rref()
pprint(R)
print('rank', len(p))
# free variables:
# z = s
# w = t
# expand rows:
# x - z - 2w = 0    => x = s + 2t
# y + 2z + 3 = 0    => y = -2s - 3
s, t = symbols('s, t')
vx = Matrix([
    s + 2 * t,  # x
    2 * s - 3,  # y
    s,          # z
    t           # w
])
pprint(vx)
u = Matrix([1, -2, 1, 0])
v = Matrix([2, -3, 0, 1])
result = MatAdd(
    MatMul(s, u, evaluate=False),
    MatMul(t, v, evaluate=False),
    evaluate=False
)
pprint(result)

# B is in R4, is rank 22, and nullity is rank 2
# 4 = 2 + 2 ?

# Match the result with sympy:
# pprint(B.nullspace())
