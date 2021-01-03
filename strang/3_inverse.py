from sympy import *

a, b, c, d = symbols('a b c d')
A = Matrix([
    [a, b],
    [c, d]
])
Ai = A.inv()
# Inverse can be on either side of A to produce the same
pprint(Eq(Ai * A, A * Ai))

# This matrix has no inverse
A = Matrix([
    [1, 3],
    [2, 6]
])
# pprint(A.inv())  # Matrix det == 0; not invertible.
#
# But you can see that row 1 is a multiple of row 0,
# so using this to transform a value would lose information
# about the original value
# "You can find a vector x (other than the zero vector) where Ax = 0"
# "Cannot multiply 0 by Ai to get back to A"

A = Matrix([
    [1, 3],
    [2, 7]
])
# "Those who like columns can see that vectors (1, 2) and (3, 7)
#  point in different directions so I can get anything"
Ai = A.inv()
I = eye(2)
pprint(Eq(A * Ai, I))
# "A * column j of Ai = column j of I"
pprint(Eq(A * Ai.col(0), I.col(0)))
pprint(Eq(A * Ai.col(1), I.col(1)))
# "It's like solving a system of equations where we have two rhs instead of one"
