import numpy as np
from fractions import Fraction

m = np.array([
    [2, -1, -4, 0],
    [3, 5, 2, 5],
    [4, -3, 6, -16]
])
m = m.astype(float)
print(m)

m[1] = m[1] - Fraction(3, 2) * m[0]
print(m)

m[2] = m[2] - 2 * m[0]
print(m)

m[2] = m[2] + (1 / 6.5) * m[1]
print(m)

m[2] = m[2] / m[2, 2]
print(m)

m[1] = m[1] - m[2] * 8
print(m)

m[1] = m[1] / m[1, 1]
print(m)

m[0] = m[0] + 4 * m[2]
print(m)

m[0] = m[0] + m[1]
print(m)

m[0] = m[0] / 2
print(m)

print('final:', m[:, 3])
