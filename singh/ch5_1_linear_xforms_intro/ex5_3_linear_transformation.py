from sympy import *

A = Matrix([
    [1, 0],
    [0, -1]
])
x, y = symbols('x y')
v1 = Matrix([x, y])
v2 = A * v1
pprint([v1, v2])

