# https://docs.sympy.org/latest/tutorial/gotchas.html
from sympy import *
from sys import exit

init_printing(use_unicode=True)


def p(s):
    print('--------------------------------------------------------------------------------')
    pprint(s)


x = symbols('x')

p(Eq(x + 1, 4))
p((x + 1) ** 2 == x ** 2 + 2 * x + 1)
a = (x + 1) ** 2
b = x ** 2 + 2 * x + 1
p(simplify(a - b))
c = x ** 2 - 2 * x + 1
p(simplify(a - c))
a = cos(x) ** 2 - sin(x) ** 2
b = cos(2 * x)
p(a.equals(b))  # evaluates using random points?
p(Integer(1) / Integer(3))
p(Rational(1, 2))

exit()
