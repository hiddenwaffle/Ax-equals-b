from sympy import *

x, y, z = symbols('x y z')
Txyz = Matrix([
    [3 * x + y + z],
    [x - 3 * y - z]
])
Te1 = Txyz.subs([(x, 1), (y, 0), (z, 0)])
Te2 = Txyz.subs([(x, 0), (y, 1), (z, 0)])
Te3 = Txyz.subs([(x, 0), (y, 0), (z, 1)])
A = Matrix([
    [Te1, Te2, Te3]
])
pprint(A)
