import numpy as np

A = np.array([
    [1, 2, 0],
    [2, 5, -1],
    [4, 10, -1]
])
B = np.array([
    [5, 2, -2],
    [-2, -1, 1],
    [0, -2, 1]
])
print(A @ B)
print(B @ A)
