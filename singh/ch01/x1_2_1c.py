import numpy as np
from fractions import Fraction
from util.frac import pretty_fractions

pretty_fractions()

m = np.array([
    [2, 2, 1, 10],
    [1, -3, 4, 0],
    [3, -1, 6, 12]
])
m = m.astype(float)
print(m)

m[1] = m[1] - Fraction(1, 2) * m[0]
print(m)

m[2] = m[2] - Fraction(3, 2) * m[0]
print(m)

m[2] = m[2] - m[1]
print(m)

m[1] = m[1] - m[2] * 3.5
print(m)

m[1] = m[1] / -4
print(m)

m[0] = m[0] - m[2]
print(m)

m[0] = m[0] - 2 * m[1]
print(m)

m[0] = m[0] / 2
print(m)

print('final:', m[:, 3])
