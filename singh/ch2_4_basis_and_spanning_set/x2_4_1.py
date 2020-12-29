import numpy as np
from sympy import *

print('a')
e1 = Matrix([1, 0])
e2 = Matrix([0, 1])
m = Matrix.hstack(e1, e2, zeros(2, 1))
pprint(m)
# Already in rref, and the rows = 0s
print('spans R2')

print('b')
u = Matrix([1, 1])
v = Matrix([-1, 1])
m = Matrix.hstack(u, v, zeros(2, 1))
m, _ = m.rref()
pprint(m)
print('spans R2')

print('c')
u = Matrix([2, 2])
v = Matrix([-1, -1])
m = Matrix.hstack(u, v, zeros(2, 1))
m, _ = m.rref()
pprint(m)
print('does not span R2')

print('d')
u = Matrix([1, 2])
v = Matrix([-1, 10])
m = Matrix.hstack(u, v, zeros(2, 1))
m, _ = m.rref()
pprint(m)
print('spans R2')
