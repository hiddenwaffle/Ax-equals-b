from sympy import *

a, b, c, d, e, f, g, h, i = symbols('a b c d e f g h i')
A = Matrix([
    [a, b, c],
    [d, e, f],
    [g, h, i]
])
pprint(A.det())
