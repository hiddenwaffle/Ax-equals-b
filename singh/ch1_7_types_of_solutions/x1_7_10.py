import numpy as np
from sympy import Matrix

m = Matrix([
    [1, 1, 0, 1, 1, 0, 0, 0, 0, 19],
    [0, 1, 1, 0, 1, 1, 0, 0, 0, 18],
    [0, 0, 0, 1, 1, 0, 1, 1, 0, 28],
    [0, 0, 0, 0, 1, 1, 0, 1, 1, 25]
])
m, p = m.rref()
m = np.array(m)
print(m)
print(p)
# Answer
# x1 - a - c + e = -2   => x1 = a + c - e - 2
# x2 + a - d - e = -7   => x2 = -a + d + e - 7
# x3 = a
# x4 - b + c - e = 3    => x4 = b - c + e + 3
# x5 + b + d + e = 25   => x5 = -b -d -e + 25
# x6 = b
# x7 = c
# x8 = d
# x9 = e
