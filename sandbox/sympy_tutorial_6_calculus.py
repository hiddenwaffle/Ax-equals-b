# https://docs.sympy.org/latest/tutorial/calculus.html
from sympy import *
from sys import exit

init_printing(use_unicode=True)


def p(s):
    print('--------------------------------------------------------------------------------')
    pprint(s)


x, y, z = symbols('x y z')
p(diff(cos(x), x))
p(diff(exp(x ** 2), x))
p(diff(x ** 4, x, x, x))
p(diff(x ** 4, x, 3))

expr = exp(x * y * z)
p(diff(expr, x, y, y, z, z, z, z))
p(diff(expr, x, y, 2, z, 4))
p(diff(expr, x, y, y, z, 4))
p(expr.diff(x, y, y, z, 4))

deriv = Derivative(expr, x, y, y, z, 4)
p(deriv)
p(deriv.doit())

m, n, a, b = symbols('m n a b')
expr = (a * x + b) ** m
p(expr.diff((x, n)))

p(integrate(cos(x), x))
p(integrate(exp(-x), (x, 0, oo)))
p(integrate(exp(-x ** 2 - y ** 2), (x, -oo, oo), (y, -oo, oo)))
expr = integrate(x ** x, x)
p(expr)
expr = Integral(log(x) ** 2, x)
p(expr)
p(expr.doit())

integ = Integral(x ** y * exp(-x), (x, 0, oo))
p(integ)
p(integ.doit())

p(limit(sin(x) / x, x, 0))
expr = x ** 2 / exp(x)
p(expr.subs(x, oo))
p(limit(expr, x, oo))
expr = Limit((cos(x) - 1) / x, x, 0)
p(expr)
p(expr.doit())
p(limit(1/x, x, 0, '+'))
p(limit(1/x, x, 0, '-'))

expr = exp(sin(x))
p(expr.series(x, 0, 4))
p(x + x ** 3 + x ** 6 + O(x ** 4))
p(x * O(1))
p(expr.series(x, 0, 4).removeO())
p(exp(x - 6).series(x, x0=6))

f, g = symbols('f g', cls=Function)
p(differentiate_finite(f(x) * g(x)))

f = Function('f')
dfdx = f(x).diff(x)
p(dfdx.as_finite_difference())

f = Function('f')
d2fdx2 = f(x).diff(x, 2)
h = Symbol('h')
p(d2fdx2.as_finite_difference([-3 * h, -h, 2 * h]))
p(finite_diff_weights(2, [-3, -1, 2], 0)[-1][-1])

x_list = [-3, 1, 2]
y_list = symbols('a b c')
p(apply_finite_diff(1, x_list, y_list, 0))

exit()
