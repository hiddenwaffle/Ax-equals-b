from itertools import permutations
from sympy import *

e1 = Matrix([[1, 0, 0]]).T
e2 = Matrix([[0, 1, 0]]).T
e3 = Matrix([[0, 0, 1]]).T
B = [e1, e2, e3]

# e1, e2, and e3 are orthogonal to each other
for a, b in list(permutations(B, 2)):
    pprint(a.T * b)

# e1, e2, and e3 are normalized
pprint(e1.norm())
pprint(e2.norm())
pprint(e2.norm())
