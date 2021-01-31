from sympy import *

A = Matrix([
    [-2, -4],
    [1, 3]
])
charpoly = A.charpoly()
pprint(charpoly)
I = eye(2)
# 0 = A ** 2 + A - 2 * I  # in the form of the charpoly
A2 = A + 2 * I
A3 = A ** 2 + 2 * A
A3 = A + 2 * I + 2 * A  # substituting A2 for A ** 2, and continue this pattern
A3 = 3 * A + 2 * I
A4 = 3 * A ** 2 + 2 * A
A4 = 3 * (A + 2 * I) + 2 * A
A4 = 3 * A + 6 * I + 2 * A
A4 = 5 * A + 6 * I
pprint(A4)  # Done

pprint(A * A * A * A)  # Compare to the manual method, same
