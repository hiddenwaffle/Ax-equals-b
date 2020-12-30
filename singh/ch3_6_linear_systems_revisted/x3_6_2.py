from sympy import *

print('a')
A = Matrix([
    [1, -2, -3],
    [4, -5, -6],
    [7, -8, -9]
])
R, _ = A.rref()
pprint(R)
# x + z = 0     => x + s = 0    => x = -s
# y + 2z = 0    => y + 2s = 0   => y = -2s
# z = s
s = symbols('s')
u = Matrix([-s, -2 * s, s])
u = MatMul(s, u / s)
pprint(u)

print('b')
A = Matrix([
    [2, -2, -2],
    [4, -4, -4],
    [8, -8, -8]
])
R, _ = A.rref()
pprint(R)
# x - y - z = 0     => x - s - t = 0    => x = s + t
# y = s
# z = t
s, t = symbols('s t')
u = Matrix([s + t, s, t])
pprint(u)
# factor out
pprint(MatAdd(
    MatMul(s, Matrix([1, 1, 0])),
    MatMul(t, Matrix([1, 0, 1]))
))

pprint('c')
A = Matrix([
    [2, 9, -3],
    [5, 6, -1],
    [9, 8, -9]
])
R, _ = A.rref()
pprint(R)
# x = y = z = 0
# (zero vector)

pprint('d')
A = Matrix([
    [-3, 1, -1],
    [2, 5, -7],
    [4, 8, -4]
])
R, _ = A.rref()
pprint(R)
# x = y = z = 0
# (zero vector)
