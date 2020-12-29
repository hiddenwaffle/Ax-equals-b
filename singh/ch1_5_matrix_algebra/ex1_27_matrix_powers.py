import numpy as np
from numpy.linalg import matrix_power

A = np.array([
    [-3, 7],
    [1, 8]
])
B = np.array([
    [5, 9],
    [2, 3]
])

print('a')
print(matrix_power(A, 2))
print('b')
print(matrix_power(B, 2))
print('c')
print(2 * A @ B)
print('d')
print(matrix_power((A + B), 2))
print('e')
print(matrix_power(A, 2) + 2 * A @ B + matrix_power(B, 2))
print('f - because order matters when @ing')
