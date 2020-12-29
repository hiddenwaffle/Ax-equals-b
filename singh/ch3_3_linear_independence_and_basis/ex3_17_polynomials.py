from sympy import *

t, k1, k2, k3 = symbols('t k1 k2 k3')
p = t ** 2 + 3 * t - 1
q = 2 * t ** 2 + 7 * t + 5
r = 7

result = linsolve([
    k1 * p,
    k2 * q,
    k3 * r
], [k1, k2, k3])
pprint(result)
# when k1, k2, and k3 = 0, the equality is true
