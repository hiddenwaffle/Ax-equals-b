from sympy import *

# 3x3 elimination, to get a zero in the right places, is:
# E32 * E31 * E21 * A = U
# (given no row exchanges)
# But how to express this with the Es on the rhs?
# A = _________ U
#         ^--------- It would be the inverse of the Es:
# A = E21i * E31i * E32i * U
# But why the product of E inverses more desirable than the product of Es?

print('Gettng E without inverses:')
E32 = Matrix([
    [1, 0, 0],
    [0, 1, 0],
    [0, -5, 1]
])
E21 = Matrix([
    [1, 0, 0],
    [-2, 1, 0],
    [0, 0, 1]
])
E = E32 * E21  # Notice that this gives 1s on the diagonal and 0s above
pprint(E)
# It says, "I'm subtracting rows from lower rows", "nothing is moving upwards"
# But we don't want the 10 in the lower left corner (TODO: Why?)

print('Getting inverses of the elementary matrices')
# Remember that with these elementary matrices, each's inverse
# is the same thing but with a negated sign -- instead of taking away
# rows, you're adding them, and vice versa
E32i = E32.inv()
pprint('E32 vs E32i')
pprint([E32, E32])
E21i = E21.inv()
pprint('E21 vs E21i')
pprint([E21, E21i])
print('E21i * E32i')
print('Getting L with the inverses')
L = E21i * E32i
pprint(L)

# A = LU
# If no row exchanges, multipliers go "directly" into L
# "As you are going along carrying out the multiplication,
#  you can 'forget' parts of A as you are getting L and U"
#        ^^^^^^^^^^^ I think is what was said (?)
