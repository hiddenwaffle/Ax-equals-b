from sympy import *

x, y, z = symbols('x y z')
e = [x * 1 + y * 1 + z * 1]
pprint(nonlinsolve(e, [x, y, z]))
