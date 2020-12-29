from sympy import *

A = Matrix([
    [1, 2, 3, 4, 5, 6, 7],
    [8, 9, 10, 11, 12, 13, 14],
    [15, 16, 17, 18, 19, 20, 21],
    [22, 23, 24, 25, 26, 27, 28],
    [29, 30, 31, 32, 33, 34, 35]
])
R, p = A.rref()
pprint(R)
print('rank', len(p))
# a1 - a3 - 2 * a4 - 3 * a5 - 4 * a6 - 5 * a7 = 0
#   => a1 = a3 + 2 * a4 + 3 * a5 + 4 * a6 + 5 * a7
# a2 + 2 * a3 + 3 * a4 + 4 * a5 + 5 * a6 + 6 * a7 = 0
#   => a2 = -2 * a3 - 3 * a4 - 4 * a5 - 5 * a6 - 6 * a7
# a3, a4, a5, a6, a7 are all free
print('nullity', 5)
pprint(A.nullspace())
