from sympy import *

# Elimination with Matrices
# Construct elementary matrices and multiply them by A
A = Matrix([
    [1, 2, 1],
    [3, 8, 1],
    [0, 4, 1]
])
# subtract 3x of first row from second
E21 = Matrix([
    [1, 0, 0],
    [-3, 1, 0],
    [0, 0, 1]
])
# subtract 2x of second row from third
E32 = Matrix([
    [1, 0, 0],
    [0, 1, 0],
    [0, -2, 1]
])
# divide third row by 5
E33 = Matrix([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, Rational(1, 5)]
])
# add 2x third row to second row
E23 = Matrix([
    [1, 0, 0],
    [0, 1, 2],
    [0, 0, 1]
])
# divide second row by 2
E22 = Matrix([
    [1, 0, 0],
    [0, Rational(1, 2), 0],
    [0, 0, 1]
])
# subtract third row from first and 2x second row from first
E12_13 = Matrix([
    [1, -2, -1],
    [0, 1, 0],
    [0, 0, 1]
])
E = E12_13 * E22 * E23 * E33 * E32 * E21
print('elementary matrices, combined together')
pprint(E)
print('combined elementary matrices, combined with A')
pprint(E * A)
