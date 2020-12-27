from sympy import *

print('a')
A = Matrix([
    [1, 1, 0],
    [2, 5, 0],
    [3, 4, 9]
])
Ai = A.inv()
b = Matrix([1, 3, 4])
x = Ai @ b
pprint(x)
# b is in the space spanned by the columns of A

print('b')
A = Matrix([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
# Ai = A.inv()  # Not invertible
# Means that Ax=b is inconsistent, so there is no vector x
# that can be transformed by A into b
