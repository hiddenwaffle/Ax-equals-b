import numpy as np
from fractions import Fraction

m = np.array([
    [1, 2, -3, 3],
    [2, -1, -1, 11],
    [3, 2, 1, -5]
])
print(m, "\n", '---')

m[1] = m[1] - 2 * m[0]
print(m, "\n", '---')

m[2] = m[2] - 3 * m[0]
print(m, "\n", '---')

m[2] = m[2] - m[1] * Fraction(4, 5)
print(m, "\n", '---')

m[2] = m[2] / 6
print(m, "\n", '---')

m[1] = m[1] - m[2] * 5
print(m, "\n", '---')

m[1] = m[1] / -5
print(m, "\n", '---')

m[0] = m[0] - m[2] * -3
print(m, "\n", '---')

m[0] = m[0] - m[1] * 2
print(m, "\n", '---')

print(m[:, 3])
