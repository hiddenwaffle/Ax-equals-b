import numpy as np
from sympy import *

print('a')
u = Matrix([1, 2])
v = Matrix([0, 1])
m = Matrix.hstack(u, v, zeros(2, 1))
m, _ = m.rref()
pprint(m)
print('forms a basis for R2')

print('b')
u = Matrix([-2, -4])
v = Matrix([1, 2])
m = Matrix.hstack(u, v, zeros(2, 1))
m, _ = m.rref()
pprint(m)
print('does not form a basis for R2')

print('c')
u = Matrix([4, 1])
v = Matrix([1, 3])
m = Matrix.hstack(u, v, zeros(2, 1))
m, _ = m.rref()
pprint(m)
print('forms a basis for R2')

print('d')
u = Matrix([3, 5])
v = Matrix([2, 3])
m = Matrix.hstack(u, v, zeros(2, 1))
m, _ = m.rref()
pprint(m)
print('forms a basis for R2')
