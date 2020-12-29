from sympy import *

A = Matrix([
    [1, 2, 3, 4, 5, 6],
    [27, 28, 29, 30, 31, 32],
    [15, 16, 17, 18, 19, 20],
    [31, 32, 33, 34, 35, 36],
    [45, 46, 47, 48, 49, 50]
])
pprint(A)
R, p = A.rref()
pprint(R)
pprint(p)
print(A.rank(), R.rank())  # notice that these are equal
