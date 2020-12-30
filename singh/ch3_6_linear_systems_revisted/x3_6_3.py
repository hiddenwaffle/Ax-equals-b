from sympy import *

print('a')
A = Matrix([
    [1, -2, -3],
    [4, -5, -6],
    [7, -8, -9]
])
R, _ = A.rref()
pprint(R)
print('rank 2')
# x + z = 0     => x = -s
# y + 2z = 0    => y = -2s
# z = s
s = symbols('s')
u = Matrix([-s, -2 * s, s])
u = MatMul(s, u / s)
pprint(u)
print('nullity 1')

print('b')
B = Matrix([
    [2, -2, -2],
    [4, -4, -4],
    [8, -8, -8]
])
R, _ = B.rref()
pprint(R)
# x - y - z = 0     => x = s + t
# y = s
# z = t
s, t = symbols('s t')
u = Matrix([s + t, s, t])
pprint(u)
pprint(MatAdd(
    MatMul(s, Matrix([1, 1, 0])),
    MatMul(t, Matrix([1, 0, 1]))
))
print('rank 1 nullity 2')
# pprint(B.nullspace())

print('c')
C = Matrix([
    [2, 9, -3],
    [5, 6, -1],
    [9, 8, -9]
])
R, _ = C.rref()
pprint(R)
print('rank 3 nullity 0')
pprint(C.nullspace())

print('d')
D = Matrix([
    [-3, 1, -1],
    [2, 5, -7],
    [4, 8, -4]
])
R, _ = D.rref()
pprint(R)
print('rank 3 nullity 0')
pprint(C.nullspace())
