import numpy as np

A = np.array([
    [9, 2],
    [13, 3]
])
B = np.array([
    [3, -2],
    [-13, 9]
])
print('a')
print(A @ B)

A = np.array([
    [1, 2, 3],
    [0, 1, 4],
    [0, 0, 1]
])
B = np.array([
    [1, -2, 5],
    [0, 1, -4],
    [0, 0, 1]
])
print('b')
print(A @ B)

A = np.array([
    [1, 0, 2],
    [2, -1, 3],
    [4, 1, 8]
])
B = np.array([
    [-11, 2, 2],
    [-4, 0, 1],
    [6, -1, -1]
])
print('c')
print(A @ B)
