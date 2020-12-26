import numpy as np
from sympy import Matrix

m = Matrix([
    [1, 1, 1, 0, 0, 0, 6],
    [0, 0, 0, 1, 1, 1, 15],
    [1, 0, 0, 1, 0, 0, 5],
    [0, 1, 0, 0, 1, 0, 7],
    [0, 0, 1, 0, 0, 1, 9]
])
m, p = m.rref()
m = np.array(m)
print(m)
# x1 - x5 - x6 = -10
# x2 + x5 = 7
# x3 + x6 = 9
# x4 + x5 + x6 = 15
# Answer:
# x1 = s + t - 10
# x2 = 7 - s
# x3 = 9 - t
# x4 = 15 - s - t
# x5 = s
# x6 = t
