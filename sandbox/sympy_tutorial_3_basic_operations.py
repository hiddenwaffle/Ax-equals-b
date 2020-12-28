# https://docs.sympy.org/latest/tutorial/basic_operations.html
import numpy as np
from sympy import *
from sys import exit

init_printing(use_unicode=True)


def p(s):
    print('--------------------------------------------------------------------------------')
    pprint(s)


x, y, z = symbols('x y z')

expr = cos(x) + 1
p(expr.subs(x, y))
p(expr.subs(x, 0))

expr = x ** y
p(expr)
expr = expr.subs(y, x ** y)
pprint(expr)
expr = expr.subs(y, x ** y)
pprint(expr)
expr = expr.subs(y, x ** y)
pprint(expr)

expr = sin(2 * x) + cos(2 * x)
p(expand_trig(expr))
p(expr.subs(sin(2 * x), 2 * sin(x) * cos(x)))

expr = cos(x)
p(expr.subs(x, 0))
p(expr)

expr = x ** 3 + 4 * x * y - z
p(expr.subs([(x, 2), (y, 4), (z, 0)]))

expr = x ** 4 - 4 * x ** 3 + 4 * x ** 2 - 2 * x + 3
replacements = [(x ** i, y ** i) for i in range(5) if i % 2 == 0]
p(replacements)
p(expr.subs(replacements))

str_expr = 'x ** 2 + 3 * x - 1 / 2'
expr = sympify(str_expr)
p(expr)
p(expr.subs(x, 2))

expr = sqrt(8)
p(expr.evalf())

p(pi.evalf(100))

expr = cos(2 * x)
p(expr.subs([(x, 2.4)]))
p(expr.evalf(subs={x: 2.4}))

one = cos(1) ** 2 + sin(1) ** 2
p((one - 1).evalf())
p((one - 1).evalf(chop=True))

a = np.arange(10)
expr = sin(x)
f = lambdify(x, expr, 'numpy')
p(f(a))

f = lambdify(x, expr, 'math')
p(f(0.1))


def mysin(x):
    """Only accurate for small x, lol"""
    return x


f = lambdify(x, expr, {'sin': mysin})
p(f(0.01))

exit()
