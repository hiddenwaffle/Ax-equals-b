from sympy import *

x, y = symbols('x y')
Txy = Matrix([
    [2 * x - y],
    [x + 3 * y]
])
Te1 = Txy.subs([(x, 1), (y, 0)])
Te2 = Txy.subs([(x, 0), (y, 1)])
A = Matrix([
    [Te1, Te2]
])
pprint(A)
