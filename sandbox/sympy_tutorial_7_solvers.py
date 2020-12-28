# https://docs.sympy.org/latest/tutorial/solvers.html
from sympy import *
from sys import exit

init_printing(use_unicode=True)


def p(s):
    print('--------------------------------------------------------------------------------')
    pprint(s)


x, y, z = symbols('x y z')

p(solveset(Eq(x ** 2, 1), x))
p(solveset(Eq(x ** 2 - 1, 0), x))
p(solveset(x ** 2 - 1, x))

p(solveset(x ** 2 - x, x))
p(solveset(x - x, x, domain=S.Reals))
p(solveset(sin(x) - 1, x, domain=S.Reals))
p(solveset(exp(x), x))
p(solveset(cos(x) - x, x))

p(linsolve([
    x + y + z - 1,
    x + y + 2 * z - 3
], (x, y, z)))
p(linsolve(Matrix([
    [1, 1, 1, 1],
    [1, 1, 2, 3],
]), (x, y, z)))
M = Matrix((
    [1, 1, 1, 1],
    [1, 1, 2, 3]
))
system = A, b = M[:, :-1], M[:, -1]  # i.e., system is Ax=b of M
p(linsolve(system, x, y, z))

a, b, c, d = symbols('a, b, c, d', real=True)
p(nonlinsolve([
    a ** 2 + a,
    a - b
], [a, b]))
p(nonlinsolve([
    x * y - 1,
    x - 2
], x, y))
p(nonlinsolve([
    x ** 2 + 1,
    y ** 2 + 1
], [x, y]))
system = [
    x ** 2 - 2 * y ** 2,
    x * y - 2
]
vars = [x, y]
p(nonlinsolve(system, vars))
system = [
    exp(x) - sin(y),
    1 / y - 3
]
p(nonlinsolve(system, vars))
p(nonlinsolve([
    x * y,
    x * y - x
], [x, y]))
system = [a ** 2 + a * c, a - b]
p(nonlinsolve(system, [a, b]))

p(solveset(x ** 3 - 6 * x ** 2 + 9 * x, x))
p(roots(x ** 3 - 6 * x ** 2 + 9 * x, x))

f, g = symbols('f g', cls=Function)
p(f(x))
p(f(x).diff(x))
diffeq = Eq(f(x).diff(x, x) - 2 * f(x).diff(x) + f(x), sin(x))
p(diffeq)
p(dsolve(diffeq, f(x)))
p(dsolve(f(x).diff(x) * (1 - sin(f(x))) - 1, f(x)))  # slow

exit()
