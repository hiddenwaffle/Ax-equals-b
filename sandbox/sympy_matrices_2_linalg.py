# https://docs.sympy.org/latest/modules/matrices/matrices.html#linear-algebra
from sympy import *

init_printing(use_unicode=True)


def p(s):
    print('--------------------------------------------------------------------------------')
    pprint(s)


M = Matrix([
    [1, 2, 3],
    [3, 6, 2],
    [2, 0, 1]
])
p(M.det())

M2 = eye(3)
p(M2.det())

M3 = Matrix([
    [1, 0, 0],
    [1, 0, 0],
    [1, 0, 0]
])
p(M3.det())

p(M2.inv())
p(M2.inv(method='LU'))
p(M.inv(method='LU'))
p(M * M.inv(method='LU'))

A = Matrix([
    [1, 1, 1],
    [1, 1, 3],
    [2, 3, 4]
])
Q, R = A.QRdecomposition()
p(Q)
p(R)
p(Q * R)

A = Matrix([
    [2, 3, 5],
    [3, 6, 2],
    [8, 3, 6]
])
x = Matrix(3, 1, [3, 7, 5])
b = A * x
soln = A.LUsolve(b)
p(soln)

L = [Matrix([2, 3, 5]), Matrix([3, 6, 2]), Matrix([8, 3, 6])]
out1 = GramSchmidt(L)
out2 = GramSchmidt(L, True)
for i in out1:
    print(i)
for i in out2:
    print(i)
p(out1[0].dot(out1[1]))
p(out1[0].dot(out1[2]))
p(out1[1].dot(out1[2]))
p(out2[0].norm())
p(out2[1].norm())
p(out2[2].norm())
