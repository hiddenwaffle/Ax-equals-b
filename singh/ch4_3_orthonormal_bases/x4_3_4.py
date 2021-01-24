from sympy import *

print('a')
v1 = Matrix([1, 0, 1])
v2 = Matrix([3, 1, 1])
v3 = Matrix([-1, -1, -1])
result = GramSchmidt([v1, v2, v3])
pprint(result)

print('b')
v1 = Matrix([2, 2, 2])
v2 = Matrix([-1, 0, -1])
v3 = Matrix([-1, 2, 3])
result = GramSchmidt([v1, v2, v3])
pprint(result)

print('c')
v1 = Matrix([1, 2, 0])
v2 = Matrix([2, 0, 2])
v3 = Matrix([1, 0, 3])
result = GramSchmidt([v1, v2, v3])
pprint(result)
