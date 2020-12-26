import numpy as np
from sympy import *

m = Matrix([
    [1, 0, 2, 1, 0, 0],
    [2, -1, 3, 0, 1, 0],
    [4, 1, 8, 0, 0, 1]
])
m, p = m.rref()
# Get the right-side only
m.col_del(0)
m.col_del(0)
m.col_del(0)
pprint(m)
m = np.array(m, dtype='int')
print(m)
