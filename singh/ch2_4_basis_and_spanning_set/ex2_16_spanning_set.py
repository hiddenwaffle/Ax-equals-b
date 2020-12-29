from sympy import *

a, b, c = symbols('a b c')
v = Matrix([a, b, c])
e1 = Matrix([1, 0, 0])
e2 = Matrix([0, 1, 0])
e3 = Matrix([0, 0, 1])

pprint(v)
pprint(a * e1 + b * e2 + c * e3)
# they are the same
