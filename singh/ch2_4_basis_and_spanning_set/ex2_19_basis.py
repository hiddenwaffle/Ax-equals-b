from sympy import *

print('i')
u = Matrix([1, 1])
v = Matrix([1, -1])
a, b = symbols('a b')
w = Matrix([a, b])

m = Matrix.hstack(u, v, w)
m, _ = m.rref()
pprint(m)

k, c = m.col(2)
pprint(k)
pprint(c)

print('ii')
# seems like rref shows that they no row is a scalar multiple of another?
