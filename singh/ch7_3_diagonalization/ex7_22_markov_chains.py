from sympy import *

T = Matrix([
    [0.6, 0.5],
    [0.4, 0.5]
])
x = Matrix([[90, 10]]).T

print('i')
P, D = T.diagonalize()
Pi = P.inv()
# pprint(P * D * Pi)  # = T
D10 = D.copy()
D10[0, 0] **= 10
D10[1, 1] **= 10
T10 = P * D10 * Pi
x10 = T10 * x
pprint(x10)
