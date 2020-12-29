import numpy as np

A = np.array([
    [2, 3],
    [6, 7],
    [1, 2]
])
B = np.array([
    [1, 2],
    [3, 4]
])
C = np.array([
    [5, 6],
    [7, 8]
])
result1 = A @ (B + C)
result2 = A @ B + A @ C
print(result1)
print(result2)
print(np.array_equal(result1, result2))
