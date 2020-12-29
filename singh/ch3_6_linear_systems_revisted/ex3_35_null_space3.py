from sympy import *

C = Matrix([
    [1, 3],
    [5, 15]
])
pprint(C)
# find the null space, nullity, and rank of C

R, p = C.rref()
pprint(R)
print('rank', len(p))
# x + 3y = 0    => x = -3y   => x = -3s
# y = s
s = symbols('s')
vx = Matrix([
    -3 * s,
    s
])
pprint(vx)
u = vx / s
print('null space:')
pprint(MatMul(s, u, evaluate=False))
print('nullity: 1')

# check with sympy
pprint(C.nullspace())
