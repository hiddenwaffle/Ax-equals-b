import numpy as np
from util.frac import pretty_fractions

# Avoid back substitution by carrying out Gauss-Jordan elimination

pretty_fractions()

a1 = np.array([
    [1, 5, -3, -9],
    [0, -13, 5, 37],
    [0, 0, 5, -15]
])
print(a1, "\n", '---')

a2 = np.array([
    a1[0],
    a1[1],
    a1[2] / a1[2, 2]
])
print(a2, "\n", '---')

a3 = np.array([
    a2[0],
    a2[1] - a2[1, 2] * a2[2],
    a2[2]
])
print(a3, "\n", '---')

a4 = np.array([
    a3[0],
    a3[1] / a3[1, 1],
    a3[2]
])
print(a4, "\n", '---')

a5 = np.array([
    a4[0] - a4[0, 2] * a4[2],
    a4[1],
    a4[2]
])
print(a5, "\n", '---')

final = np.array([
    a5[0] - a5[0, 1] * a4[1],
    a5[1],
    a5[2]
])
print(final, "\n", '---')

# Use backsubstitution to solve
x = final[0, 3]
y = final[1, 3]
z = final[2, 3]
print(f'x: {x}, y: {y}, z: {z}')
