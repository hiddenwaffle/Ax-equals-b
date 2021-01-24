from sympy import *

A = Matrix([
    [1, 1],
    [-1, 1]
])
x, y = symbols('x y')
v = Matrix([[x, y]]).T
O = zeros(2, 1)
eq = Eq(MatMul(A, v), O)
pprint(eq)
pprint(solve(eq, [x, y]))
