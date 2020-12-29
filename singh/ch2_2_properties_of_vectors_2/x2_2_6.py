from sympy import *

k = symbols('k')
e = sqrt((1 / sqrt(2))**2 + Rational(1, 2)**2 + k**2) - 1
pprint(e)
pprint(solveset(e, k))
