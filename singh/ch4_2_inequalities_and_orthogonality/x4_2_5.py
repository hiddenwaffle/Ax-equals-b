from sympy import *

k = symbols('k')

print('a')
u = Matrix([[1, 2, 3, 4]]).T
v = Matrix([[-2, 3, k, 5]]).T
pprint(u.T * v)
pprint(u.T * v.subs([(k, -8)]))

print('b')
u = Matrix([[k, -1, k, 1]]).T
v = Matrix([[2, 4, k, 5]]).T
p = (u.T * v)[0]
pprint(p)
pprint(factor(p))
pprint(u.T.subs([(k, -1)]) * v.subs([(k, -1)]))
