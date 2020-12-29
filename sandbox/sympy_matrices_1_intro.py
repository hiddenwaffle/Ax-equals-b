# https://docs.sympy.org/latest/modules/matrices/matrices.html
from sympy import *
from sys import exit

init_printing(use_unicode=True)


def p(s):
    print('--------------------------------------------------------------------------------')
    pprint(s)


M = Matrix([
    [1, 0, 0],
    [0, 0, 0]
])
p(M)

p(Matrix([
    M,
    (0, 0, -1)
]))

p(Matrix([[1, 2, 3]]))
p(Matrix([1, 2, 3]))
p(Matrix(2, 3, [1, 2, 3, 4, 5, 6]))


def f(i, j):
    if i == j:
        return 1
    else:
        return 0


p(Matrix(4, 4, f))
p(Matrix(3, 4, lambda i, j: 1 - (i + j) % 2))

p(eye(4))
p(zeros(2))
p(zeros(2, 5))
p(ones(3))
p(ones(1, 3))
p(diag(1, Matrix([[1, 2], [3, 4]])))

M = Matrix(2, 3, [1, 2, 3, 4, 5, 6])
p(M[4])
p(M[1, 2])
p(M[0, 0])
p(M[1, 1])
p(M[0:2, 0:2])
p(M[2:2, 2])
p(M[:, 2])
p(M[:1, 2])
p(Matrix(0, 3, [])[:, 1])
M2 = M[:, :]
M2[0, 0] = 100
p(M[0, 0] == 100)
M = Matrix([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])
p(M)
M[2, 2] = M[0, 3] = 0
p(M)
M = Matrix([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])
M[2:, 2:] = Matrix(2, 2, lambda i, j: 0)
p(M)

M = Matrix([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
p(M - M)
p(M + M)
p(M * M)
M2 = Matrix(3, 1, [1, 5, 0])
p(M * M2)
p(M ** 2)
M.row_del(0)
p(M)
M.col_del(1)
p(M)
v1 = Matrix([1, 2, 3])
v2 = Matrix([4, 5, 6])
v3 = v1.cross(v2)
p(v1.dot(v2))
p(v2.dot(v3))
p(v1.dot(v3))

M1 = eye(3)
M2 = zeros(3, 4)
p(M1.row_join(M2))
M3 = zeros(4, 3)
p(M1.col_join(M3))

M = eye(3)
p(2 * M)
p(3 * M)

f = lambda x: 2 *x
p(eye(3).applyfunc(f))

x, y = symbols('x y')
m = Matrix([
    [x, y],
    [1, x * y]
]).inv('ADJ')
p(m)
gcd_of_m = gcd(tuple(m))
p(gcd_of_m)
p(m / gcd_of_m)

x = Symbol('x')
M = eye(3) * x
p(M)
p(M.subs(x, 4))
p(M.subs(x, y))
y = Symbol('y')

exit()
