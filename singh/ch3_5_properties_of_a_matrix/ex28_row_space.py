from sympy import *

A = Matrix([
    [1, 2],
    [2, 4]
])
B = Matrix([
    [-1, 3, 9],
    [-5, 2, 6]
])
C = Matrix([
    [-3, 6],
    [-5, 2],
    [-2, 7]
])

print('a')
A, p = A.rref()
pprint(A)
pprint(p)
print(pretty(A.row(0)), 'is a row space of A')

print('b')
B, p = B.rref()
pprint(B)
pprint(p)
print(pretty(B.row(0)), 'and', pretty(B.row(1)), 'form a basis for the row space of B')

print('c')
C, p = C.rref()
pprint(C)
pprint(p)
print(pretty(C.row(0)), 'and', pretty(C.row(1)), 'form a basis for the row space of C')
