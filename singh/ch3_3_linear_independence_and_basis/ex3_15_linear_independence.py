from sympy import *

x, k1, k2, k3 = symbols('x k1 k2 k3')
u = cos(x)
v = sin(x)
w = 2
lc = k1 * u + k2 * v + k3 * w
pprint(lc)
# need 3 equations so substitute 3 different values of x
lc1 = lc.subs([(x, 0)])  # eliminate the sine term
pprint(lc1)
lc2 = lc.subs([(x, pi)])
pprint(lc2)
lc3 = lc.subs([(x, pi / 2)])
pprint(lc3)
# solve
A, b = linear_eq_to_matrix([lc1, lc2, lc3], [k1, k2, k3])
Ab = Matrix.hstack(A, b)
Ab = Ab.rref()
pprint(Ab)
# k1, k2, and k3 = 0
print('u, v, and w are linearly independent')
