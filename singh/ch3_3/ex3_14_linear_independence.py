from sympy import *

A = Matrix([
    [1, 0],
    [0, 1]
])
B = Matrix([
    [0, 2],
    [2, 0]
])

# TODO:
# Show that kA + cB = 0 only when k = c = 0

k, c = symbols('k c')
combo = k * A + c * B
pprint(combo)
# equating this to the zero matrix means that:
# k = 0
# c = 0
print('A and B are linearly independent')
