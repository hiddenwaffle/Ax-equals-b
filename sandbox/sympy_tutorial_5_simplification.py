# https://docs.sympy.org/latest/tutorial/simplification.html
from sympy import *
from sys import exit

init_printing(use_unicode=True)


def p(s):
    print('--------------------------------------------------------------------------------')
    pprint(s)


x, y, z = symbols('x y z')

p(simplify(sin(x) ** 2 + cos(x) ** 2))
p(simplify((x ** 3 + x ** 2 - x - 1) / (x ** 2 + 2 * x + 1)))
p(simplify(gamma(x) / gamma(x - 2)))

p(expand((x + 1) ** 2))
p(expand((x + 2) * (x - 3)))
p(expand((x + 1) * (x - 2) - (x - 1) * x))

p(factor(x ** 3 - x ** 2 + x - 1))
p(factor(x ** 2 * z + 4 * x * y * z + 4 * y ** 2 * z))

p(factor_list(x ** 2 * z + 4 * x * y * z + 4 * y ** 2 * z))

p(expand((cos(x) + sin(x)) ** 2))
p(factor(cos(x) ** 2 + 2 * cos(x) * sin(x) + sin(x) ** 2))

expr = x * y + x - 3 + 2 * x ** 2 - z * x ** 2 + x ** 3
p(expr)
collected_expr = collect(expr, x)
p(collected_expr)
p(collected_expr.coeff(x, 2))

p(cancel((x ** 2 + 2 * x + 1) / (x ** 2 + x)))
expr = 1 / x + (3 * x / 2 - 2) / (x - 4)
p(expr)
p(cancel(expr))

expr = (x * y ** 2 - 2 * x * y * z + x * z ** 2 + y ** 2 - 2 * y * z + z ** 2) / (x ** 2 - 1)
p(expr)
p(cancel(expr))
p(factor(expr))

expr = (4 * x ** 3 + 21 * x ** 2 + 10 * x + 12) / (x ** 4 + 5 * x ** 3 + 5 * x ** 2 + 4 * x)
p(expr)
p(apart(expr))

p(acos(x))
p(cos(acos(x)))
p(asin(1))

p(trigsimp(sin(x) ** 2 + cos(x) ** 2))
p(trigsimp(sin(x) ** 4 - 2 * cos(x) ** 2 * sin(x) ** 2 + cos(x) ** 4))
p(trigsimp(sin(x) * tan(x) / sec(x)))
p(trigsimp(cosh(x) ** 2 + sinh(x) ** 2))
p(trigsimp(sinh(x) / tanh(x)))

p(expand_trig(sin(x + y)))
p(trigsimp(sin(x) * cos(y) + sin(y) * cos(x)))

x, y = symbols('x y', positive=True)
a, b = symbols('a b', real=True)
z, t, c = symbols('z t c')

p(sqrt(x) == x ** Rational(1, 2))

p(powsimp(x ** a * x ** b))
p(powsimp(x ** a * y ** a))
p(powsimp(t ** c * z ** c))
p(powsimp(t ** c * z ** c, force=True))

p((z * t) ** 2)
p(sqrt(x * y))

p(powsimp(z ** 2 * t ** 2))
p(powsimp(sqrt(x) * sqrt(y)))

p(expand_power_exp(x ** (a + b)))
p(expand_power_base((x * y) ** a))
p(expand_power_base((z * t) ** c))
p(expand_power_base((z * t) ** c, force=True))
p(x ** 2 * x ** 3)
p(expand_power_exp(x ** 5))

p(powdenest((x ** a) ** b))
p(powdenest((z ** a) ** b))
p(powdenest((z ** a) ** b, force=True))

x, y = symbols('x y', positive=True)
n = symbols('n', real=True)

p(expand_log(log(x * y)))
p(expand_log(log(x / y)))
p(expand_log(log(x ** 2)))
p(expand_log(log(x ** n)))
p(expand_log(log(z * t)))

p(expand_log(log(z ** 2)))
p(expand_log(log(z ** 2), force=True))

p(logcombine(log(x) + log(y)))
p(logcombine(n * log(x)))
p(logcombine(n * log(z)))
p(logcombine(n * log(z), force=True))

x, y, z = symbols('x y z')
k, m, n = symbols('k m n')

p(factorial(n))
p(binomial(n, k))
p(gamma(z))
p(hyper([1, 2], [3], z))

p(tan(x).rewrite(sin))
p(factorial(x).rewrite(gamma))

p(expand_func(gamma(x + 3)))
p(hyperexpand(hyper([1, 1], [2], z)))
expr = meijerg([[1], [1]], [[1], []], -z)
p(expr)
p(hyperexpand(expr))

n, k = symbols('n k', integer=True)
p(combsimp(factorial(n) / factorial(n - 3)))
p(combsimp(binomial(n + 1, k + 1) / binomial(n, k)))
p(gammasimp(gamma(x) * gamma(1 - x)))


def list_to_frac(l):
    expr = Integer(0)
    for i in reversed(l[1:]):
        expr += i
        expr = 1 / expr
    return l[0] + expr


p(list_to_frac([x, y, z]))
p(list_to_frac([1, 2, 3, 4]))

syms = symbols('a0:5')
p(syms)
a0, a1, a2, a3, a4 = syms
frac = list_to_frac(syms)
p(frac)
frac = cancel(frac)
p(frac)

# pull it back apart, but manually
l = []
frac = apart(frac, a0)
p(frac)
l.append(a0)
frac = 1 / (frac - a1)
p(frac)
l.append(a1)
frac = 1 / (frac - a2)
p(frac)
# etc...

exit()
