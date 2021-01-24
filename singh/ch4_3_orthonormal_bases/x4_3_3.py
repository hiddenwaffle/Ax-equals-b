from sympy import *

v1 = Matrix([1, 1, 1])
v2 = Matrix([1, 1, 0])
v3 = Matrix([2, 0, 0])

result = GramSchmidt([v1, v2, v3])
pprint(result)
