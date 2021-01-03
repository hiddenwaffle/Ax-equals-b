from sympy import *

# 3x3

M = Matrix([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
# "exchange rows 1 and 2"
P12 = Matrix([
    [0, 1, 0],
    [1, 0, 0],
    [0, 0, 1]
])
pprint(P12 * M)

# P12 is a rearrangement of the identity matrix
# how many possible Ps (including I) are there for an nxn matrix?
# for 3x3 it looks like 6, so maybe n! ?
# for 4x4 is looks like 24, so it must be n!

# The inverse of a P is its transpose!
pprint([
    P12.inv() * P12 * M,
    P12.T * P12 * M
])
