from sympy import *

print('a')
Q = (1 / sqrt(2)) * Matrix([
    [1, 1],
    [1, -1]
])
pprint(Q.T * Q)

print('b')
Q = (1 / 5) * Matrix([
    [3, 4],
    [4, -3]
])
pprint(Q.T * Q)

print('c')
theta = symbols('theta')
Q = Matrix([
    [cos(theta), sin(theta)],
    [sin(theta), -cos(theta)]
])
pprint(trigsimp(Q.T * Q))
