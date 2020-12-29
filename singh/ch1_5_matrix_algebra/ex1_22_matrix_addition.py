import numpy as np

# Theorem (1.12) Properties of Matrix Addition

A = np.array([
    [1, -1, 3, 7],
    [2, 9, 5, -6],
])
B = np.array([
    [7, 6, -3, 2],
    [1, 4, 5, 3]
])
C = np.array([
    [-2, -7, 8, 6],
    [3, -9, 2, 1]
])

print('a', "\n", A + B)
print('b', "\n", B + A)
print('c', "\n", (A + B) + C)
print('d', "\n", A + (B + C))
print('e', "\n", A + np.zeros_like(A))
print('f', "\n", A + A + A + A + A)
print('g', "\n", C + (-C))
