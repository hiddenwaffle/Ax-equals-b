import numpy as np
from sympy import *

print('a')
u = Matrix([2, 0, 0])
v = Matrix([0, 2, 0])
w = Matrix([0, 0, 2])
m = Matrix.hstack(u, v, w, zeros(3, 1))
m, _ = m.rref()
pprint(m)
print('spans R3')

print('b')
u = Matrix([1, 1, 1])
v = Matrix([2, 2, 2])
w = Matrix([1, 2, 3])
m = Matrix.hstack(u, v, w, zeros(3, 1))
m, _ = m.rref()
pprint(m)
print('does not span R3')

print('c')
u = Matrix([1, 1, 1])
v = Matrix([1, 1, 0])
w = Matrix([1, 0, 0])
m = Matrix.hstack(u, v, w, zeros(3, 1))
m, _ = m.rref()
pprint(m)
print('spans R3')

print('d')
u = Matrix([1, 2, 1])
v = Matrix([2, 4, 0])
w = Matrix([-2, -2, 3])
m = Matrix.hstack(u, v, w, zeros(3, 1))
m, _ = m.rref()
pprint(m)
print('spans R3')