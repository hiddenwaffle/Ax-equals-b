from sympy import *

A = Matrix([
    [2, 1],
    [8, 7]
])
U = Matrix([
    [2, 1],
    [0, 3]
])
E = Matrix([  # E21, specifically
    [1, 0],
    [-4, 1]
])
# EA = U
print(Eq(E * A, U))

# A = LU
#     ^--- what is L? It is the inverse of E
# Maybe easier to see if flipping equation around:
# LU = A
print(Eq(E.inv() * U, A))
# U stands for "upper triangular"
# L stands for "lower triangular"

# If I break it down further, we could write LU as 3 matrices: A, a diagonal matrix, and what is leftover
# (so that U turns into the last two matrices):
diagonal = Matrix([
    [2, 0],
    [0, 3]
])
leftover = Matrix([
    [1, Rational(1, 2)],
    [0, 1]
])
print(Eq(diagonal * leftover, U))
