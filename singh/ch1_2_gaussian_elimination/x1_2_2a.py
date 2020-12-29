import numpy as np
from fractions import Fraction

m = np.array([
    [1, 2, 3, 12],
    [2, -1, 5, 3],
    [3, 3, 6, 21]
])
m = m.astype(float)
print(m)

m[1] = m[1] - m[0] * 2
print(m)

m[2] = m[2] - m[0] * 3
print(m)

m[2] = m[2] - Fraction(3, 5) * m[1]
print(m)

m[2] = m[2] / -2.4
print(m)

m[1] = m[1] + m[2]
print(m)

m[1] = m[1] / -5
print(m)

m[0] = m[0] - m[2] * 3
print(m)

m[0] = m[0] - m[1] * 2
print(m)
print('final', m[:, 3])

