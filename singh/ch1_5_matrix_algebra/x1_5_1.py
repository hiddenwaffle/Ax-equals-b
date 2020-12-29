import numpy as np

A = np.array([
    [2, -2, 5],
    [0, -1, 7]
])
B = np.array([
    [-1, 3, 7],
    [2, -9, 6]
])
C = np.array([
    [9, 5, 8],
    [-6, -1, 6]
])

print('a')
print(A + B)
print('b')
print(A + (B + C))
print('c')
print(A + (B + C))
print('d')
print(B + (C + A))
print('e')
print(C + np.zeros_like(C))
print('f')
print(B + B + B + B + B)
print('g')
print(5 * B)
print('h')
print(C + (-C))
