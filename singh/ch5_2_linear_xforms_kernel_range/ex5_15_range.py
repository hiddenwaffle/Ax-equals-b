from sympy import *

a, b, c, x = symbols('a b c x')
p = a * x ** 2 + b * x + c
pprint(integrate(p, (x, 0, 1)))
# Because a b and c are real numbers, T(p) can be any real number
