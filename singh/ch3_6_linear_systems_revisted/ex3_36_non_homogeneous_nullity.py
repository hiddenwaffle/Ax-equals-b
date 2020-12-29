from sympy import *

C = Matrix([
    [1, 3, 7],
    [5, 15, 35]
])
pprint(C)
# find the null space, nullity, and rank of C

R, p = C.rref()
pprint(R)
print('rank', len(p))
# x + 3y = 7    => x = 7 -3y  => x = 7 -3s
# y = s
s = symbols('s')
vx = Matrix([
    7 - 3 * s,
    s
])
pprint(vx)
xh = MatMul(s, Matrix([-3, 1]), evaluate=False)
xp = Matrix([7, 0])
# xp shifts the line of xh 7 units to the right

# check with sympy
pprint(C.nullspace())
# what do the 0 and 1 on the bottom rows of these vectors, respecively, mean?
