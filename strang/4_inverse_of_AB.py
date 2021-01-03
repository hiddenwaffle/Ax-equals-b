from sympy import *

a, b, c, d = symbols('a b c d')
A = Matrix([
    [a, b],
    [c, d]
])
e, f, g, h = symbols('e f g h')
B = Matrix([
    [e, f],
    [g, h]
])
AB = A * B
print('AB')
pprint(AB)
pprint('AB * Bi')
pprint(simplify(AB * B.inv()))
pprint('AB * BiAi')
pprint(simplify(AB * B.inv() * A.inv()))
