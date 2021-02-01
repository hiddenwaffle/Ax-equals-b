from sympy import *

A = Matrix([
    [1, -2, 3],
    [0, 2, 5],
    [0, 0, 3]
])
P = Matrix([
    [1, -2, -7],
    [0, 1, 10],
    [0, 0, 2]
])
Pi = P.inv()
D = Pi * A * P
# Find the expected result via the SymPy built-in method:
pprint(A ** 5)
# Find it by raising each entry in D to the 5th power,
# then find A5 by using: P * D ** 5 * Pi
pprint(D)
D5 = Matrix([
    [1 ** 5, 0, 0],
    [0, 2 ** 5, 0],
    [0, 0, 3 ** 5]
])
A5 = P * D5 * Pi
pprint(A5)
# result is the expected result
