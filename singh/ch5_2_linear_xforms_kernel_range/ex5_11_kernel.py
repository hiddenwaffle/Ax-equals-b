from sympy import *

print('i')
# This matrix does this transform
# x    x
# y => y
# z    0
A = Matrix([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
])
x, y, z = symbols('x y z')
v = Matrix([[x, y, z]]).T
b = zeros(3, 1)
eq = Eq(MatMul(A, v), b)
pprint(eq)
pprint(solve(eq, [x, y, z]))  # does this imply that z = any real number?

print('ii')
u = Matrix([1, 2, 3])
v = Matrix([1, 2, 5])
pprint(A * (u - v))
