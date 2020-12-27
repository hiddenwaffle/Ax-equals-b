from sympy import *

t = symbols('t')
m = Matrix([
    [t, -1, 1, 0],
    [1, t, 1, 0],
    [1, 1, t, 0]
])
pprint(m)
m, _ = m.rref()
pprint(m)
# looks like t can be any value, but some intermediate math
# requires t to not be -1, 0, or 1
# analyze the row operations for this
# can't let a cell be zero, e.g., if t - 1 is a cell then t != 1
# same for t or t + 1

