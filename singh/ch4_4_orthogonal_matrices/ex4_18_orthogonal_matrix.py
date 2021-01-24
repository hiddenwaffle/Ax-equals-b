from sympy import *

u1 = (1 / sqrt(3)) * Matrix([[1, 1, 1]]).T
u2 = (1 / sqrt(6)) * Matrix([[1, 1, -2]]).T
u3 = (1 / sqrt(2)) * Matrix([[1, -1, 0]]).T
Q = Matrix([[u1, u2, u3]])
pprint(Q.T * Q)
