from sympy import *

a, b, c, d = symbols('a b c d')
A = Matrix([
    [a, b],
    [c, d]
])
print('Ai.T * A.T')
pprint(simplify(A.inv().T * A.T))
print('(A.T)i * A.T')
pprint(simplify(A.T.inv() * A.T))
