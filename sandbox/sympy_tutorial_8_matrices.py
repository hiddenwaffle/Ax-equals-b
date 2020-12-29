# https://docs.sympy.org/latest/tutorial/matrices.html
from sympy import *
from sys import exit

init_printing(use_unicode=True)


def p(s):
    print('--------------------------------------------------------------------------------')
    pprint(s)


p(Matrix([
    [1, -1],
    [3, 4],
    [0, 2]
]))
p(Matrix([1, 2, 3]))
M = Matrix([
    [1, 2, 3],
    [3, 2, 1]
])
N = Matrix([0, 1, 1])
p(M * N)
M = Matrix([
    [1, 2, 3],
    [-2, 0, 4]
])
p(M)
p(M.shape)
p(M.row(0))
p(M.col(-1))
M.col_del(0)
p(M)
M.row_del(1)
p(M)
M = M.row_insert(1, Matrix([[0, 4]]))
p(M)
M = M.col_insert(0, Matrix([1, -2]))
p(M)

M = Matrix([
    [1, 3],
    [-2, 3]
])
N = Matrix([
    [0, 3],
    [0, 7]
])
p(M + N)
p(M * N)
p(3 * M)
p(M**2)
p(M**-1)
# p(N**-1)  # sympy.matrices.common.NonInvertibleMatrixError: Matrix det == 0; not invertible.

M = Matrix([
    [1, 2, 3],
    [4, 5, 6]
])
p(M)
p(M.T)

p(eye(3))
p(eye(4))
p(zeros(2, 3))
p(ones(3, 2))
p(diag(1, 2, 3))
p(diag(-1, ones(2, 2), Matrix([5, 7, 5])))

M = Matrix([
    [1, 0, 1],
    [2, -1, 3],
    [4, 3, 2]
])
p(M)
p(M.det())

M = Matrix([
    [1, 0, 1, 3],
    [2, 3, 4, 7],
    [-1, -3, -3, -4]
])
p(M)
p(M.rref())

M = Matrix([
    [1, 2, 3, 0, 0],
    [4, 10, 0, 0, 1]
])
p(M.nullspace())

M = Matrix([
    [1, 1, 2],
    [2, 1, 3],
    [3, 1, 4]
])
p(M.columnspace())

M = Matrix([
    [3, -2, 4, -2],
    [5, 3, -3, -2],
    [5, -2, 2, -2],
    [5, -2, -3, 3]
])
p(M)
p(M.eigenvals())
p(M.eigenvects())

P, D = M.diagonalize()
p(P)
p(D)
p(P * D * P ** -1)
p(P * D * P ** -1 == M)

lamda = symbols('lamda')
poly = M.charpoly(lamda)
p(factor(poly.as_expr()))

exit()
