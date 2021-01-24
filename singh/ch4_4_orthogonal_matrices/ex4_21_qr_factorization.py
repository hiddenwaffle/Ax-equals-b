from sympy import *

A = Matrix([
    [1, 1, 2],
    [1, 1, 0],
    [1, 0, 0]
])
result = GramSchmidt([A.col(0), A.col(1), A.col(2)], True)
Q = Matrix([result])
print('Q')
pprint(Q)
R = Q.T * A
print('R')
pprint(R)
print('This should equal A')
pprint(Q * R)
