from sympy import *

print('a')
v1 = Matrix([1, 0, 3, 0])
v2 = Matrix([1, 2, 1, 0])
v3 = Matrix([2, 1, 0, 0])
result = GramSchmidt([v1, v2, v3])
pprint(result)

print('b')
v1 = Matrix([1, 1, 5, 2])
v2 = Matrix([-3, 3, 4, -2])
v3 = Matrix([-1, -2, 2, 5])
result = GramSchmidt([v1, v2, v3])
pprint(result)

print('c')
v1 = Matrix([1, 2, 3, 4])
v2 = Matrix([2, 1, 1, 0])
v3 = Matrix([3, 0, -1, 3])
result = GramSchmidt([v1, v2, v3])
pprint(result)
