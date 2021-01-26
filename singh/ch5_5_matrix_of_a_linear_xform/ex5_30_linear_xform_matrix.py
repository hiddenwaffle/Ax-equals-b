from sympy import *

A = Matrix([
    [2, -1],
    [1, 3]
])
x, y = symbols('x y')
u = Matrix([[x, y]]).T
pprint(A * u)
