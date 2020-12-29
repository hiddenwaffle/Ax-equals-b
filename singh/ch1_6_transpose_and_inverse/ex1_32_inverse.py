import numpy as np

A = np.array([
    [3, 7],
    [2, 5]
])
B = np.array([
    [5, -7],
    [-2, 3]
])
print(np.array_equal((A @ B), np.identity(2)))
print(np.array_equal((B @ A), np.identity(2)))
