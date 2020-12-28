# https://docs.sympy.org/latest/tutorial/intro.html
from sympy import *
from sys import exit

init_printing(use_unicode=True)


def p(s):
    print('--------------------------------------------------------------------------------')
    pprint(s)


x, y, t, nu, z = symbols('x y t nu z')
expr = x + 2 * y
p(expr)
p(x * expr)
p(expand(x * expr))
p(factor(expand(x * expr)))
p(diff(sin(x) * exp(x), x))
p(integrate(exp(x) * sin(x) + exp(x) * cos(x), x))
p(integrate(sin(x ** 2), (x, -oo, oo)))
p(limit(sin(x) / x, x, 0))
p(solve(x ** 2 - 2, x))
y = Function('y')
p(dsolve(Eq(y(t).diff(t, t) - y(t), exp(t)), y(t)))
p(Matrix([[1, 2], [2, 2]]).eigenvals())
p(besselj(nu, z).rewrite(jn))
p(latex(Integral(cos(x) ** 2, (x, 0, pi))))

exit()
