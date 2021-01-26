from sympy import *

u = Matrix([[3, 9]]).T
b1 = Matrix([[1, 1]]).T
b2 = Matrix([[1, 4]]).T
k, c = symbols('k c')
eq = Eq(k * b1 + c * b2, u)
pprint(eq)
result = solve(eq, k, c)
v = Matrix([[result[k], result[c]]]).T
pprint(v)
