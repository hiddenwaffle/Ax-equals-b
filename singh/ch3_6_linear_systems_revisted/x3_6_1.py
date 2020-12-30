from sympy import *

print('a')
M = Matrix([
    [1, 0],
    [0, 1]
])
R, _ = M.rref()
pprint(R)
print('null space is the trivial solution zero vector')
pprint(M.nullspace())

print('b')
M = Matrix([
    [1, 2],
    [2, 4]
])
R, _ = M.rref()
pprint(R)
# x + 2y = 0
# x = -2y   => x = -2s
# y = s
s = symbols('s')
u = Matrix([-2 * s, s])
u = MatMul(s, u / s, evaluate=False)
pprint(u)

print('c')
M = Matrix([
    [1, 0],
    [1, 2],
    [6, 10]
])
R, _ = M.rref()
pprint(R)
pprint(M.nullspace())
# only the trivial solution (zero vector)

print('d')
M = Matrix([
    [1, 2],
    [3, 4],
    [5, 6]
])
R, _ = M.rref()
pprint(R)
# same as (c)
