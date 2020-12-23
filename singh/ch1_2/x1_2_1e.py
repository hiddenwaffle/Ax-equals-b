import numpy as np
from fractions import Fraction

m = np.array([
    [10, 1, -5, 18],
    [-20, 3, 20, 14],
    [5, 3, 5, 9]
])
m = m.astype(float)
print(m)

m[1] = m[1] + m[0] * 2
print(m)

m[2] = m[2] - m[0] * Fraction(1, 2)
print(m)

m[2] = m[2] - m[1] * Fraction(1, 2)
print(m)

m[2] = m[2] / 2.5
print(m)

m[1] = m[1] - m[2] * 10
print(m)

m[1] = m[1] / 5
print(m)

m[0] = m[0] + m[2] * 5
print(m)

m[0] = m[0] - m[1]
print(m)

m[0] = m[0] / 10
print(m)

print('final:', m[:, 3])
# -6.2, 30, -10
