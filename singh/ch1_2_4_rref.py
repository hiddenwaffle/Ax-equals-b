from fractions import Fraction
import numpy as np
from util.frac import pretty_fractions

# Avoid back substitution by carrying out Gauss-Jordan elimination

pretty_fractions()

a1 = np.array([
    [1, 3, 2, 13],
    [0, -8, -11, -49],
    [0, 0, Fraction(45, 4), Fraction(135, 4)]
])
print(a1)
print('---')

a2 = np.array([
    a1[0],
    a1[1],
    a1[2] * Fraction(a1[2, 2].denominator, a1[2, 2].numerator)
])
print(a2)
print('---')

a3 = np.array([
    a2[0],
    a2[1] * Fraction(a2[1, 1].denominator, a2[1, 1].numerator),
    a2[2]
])
print(a3)
print('---')

a4 = np.array([
    a3[0],
    a3[1] - a3[1, 2] * a3[2],
    a3[2]
])
print(a4)
print('---')

a5 = np.array([
    a4[0] - a4[0, 1] * a4[1],
    a4[1],
    a4[2]
])
print(a5)
print('---')

a6 = np.array([
    a5[0] - a5[0, 2] * a5[2],
    a5[1],
    a5[2]
])
print(a6)
print('---')

x = a6[0, 3]
y = a6[1, 3]
z = a6[2, 3]
print(f'x: {x}, y: {y}, z: {z}')
