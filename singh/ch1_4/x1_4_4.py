import numpy as np
from fractions import Fraction

m1 = np.array([
    [3, 7],
    [2, 5]
])
m2 = np.array([
    [5, -7],
    [-2, 3]
])
print('a', "\n", m1 @ m2)

m1 = np.array([
    [3, -4],
    [-7, 11]
])
m2 = np.array([
    [11, 4],
    [7, 3]
])
print('b', "\n", Fraction(1, 5) * m1 @ m2)

m1 = np.array([
    [7, -9],
    [-5, 7]
])
m2 = np.array([
    [7, 9],
    [5, 7]
])
print('c', "\n", Fraction(1, 4) * m1 @ m2)

# it's like m2 and the scalar make up the "reciprocal" of m1
