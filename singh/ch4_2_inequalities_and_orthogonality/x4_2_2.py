from sympy import *

a, b = symbols('a b')
u = Matrix([[a, b]]).T
v = Matrix([[-b, a]]).T
pprint(u.T * v)
