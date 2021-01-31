from sympy import *

print('a')
A = Matrix([
    [2, 3],
    [-1, 5]
])
pprint(A.inv())

print('b')
B = Matrix([
    [sqrt(2), 1],
    [-1, sqrt(2)]
])
pprint(B.inv())

# print('c')
# C = Matrix([
#     [pi, pi],
#     [pi, pi]
# ])
# pprint(C.inv())  # Not invertible
