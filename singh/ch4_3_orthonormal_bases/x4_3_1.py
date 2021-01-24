from sympy import *


def orthogonal(u, v):
    return v - ((u.T * v) / u.norm() ** 2)[0] * u


print('a')
v1 = Matrix([1, 0])
v2 = Matrix([2, 1])
w1 = v1.copy()
w2 = orthogonal(w1, v2)
pprint([w1, w2])

print('b')
v1 = Matrix([1, 3])
v2 = Matrix([2, -1])
w1 = v1.copy()
w2 = orthogonal(w1, v2)
pprint([w1, w2])

print('c')
v1 = Matrix([2, 3])
v2 = Matrix([4, 5])
w1 = v1.copy()
w2 = orthogonal(w1, v2)
pprint([w1, w2])

print('d')
v1 = Matrix([-2, -5])
v2 = Matrix([-3, -1])
w1 = v1.copy()
w2 = orthogonal(w1, v2)
pprint([w1, w2])
