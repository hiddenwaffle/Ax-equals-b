from sympy import *

A = Matrix([
    [2, -1, -1],
    [2, 0, 2],
    [2, -1, 3]
])
Q = Matrix([GramSchmidt([A.col(0), A.col(1), A.col(2)], orthonormal=True)])
R = Q.T * A
print('a')
print('Q')
pprint(Q)
print('R')
pprint(R)

print('b')
b = Matrix([[-3, 8, 9]]).T
c = Q.T * b
M = R.row_join(c)
pprint(M.rref())

print('c')
b = Matrix([[-5, 12, 11]]).T
c = Q.T * b
M = R.row_join(c)
pprint(M.rref())
