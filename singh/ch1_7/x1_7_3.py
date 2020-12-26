import numpy as np
from sympy import Matrix

k = 2  # This is a guess; if had done by hand, it would have been apparent
m = Matrix([
    [2, -1, -4, k],
    [-1, 1, 2, k],
    [-1, 1, k, k]
])
m, p = m.rref()
m = np.array(m)
print(m)
print(p)
# x - 2z = 4     => x = 2z + 4
# y = 6
# Answer:
# x = 2s + 4
# y = 6
# z = s
