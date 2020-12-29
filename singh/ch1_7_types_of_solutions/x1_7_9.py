import numpy as np
from sympy import Matrix

m = Matrix([
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 16],
    [0, 0, 0, 1, 1, 1, 0, 0, 0, 21],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 8],
    [1, 0, 0, 1, 0, 0, 1, 0, 0, 17],
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 15],
    [0, 0, 1, 0, 0, 1, 0, 0, 1, 13]
])
m, p = m.rref()
m = np.array(m)
print(m)
print(p)
# etc...
