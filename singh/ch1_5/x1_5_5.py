import numpy as np

A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
B = np.array([
    [2, -1],
    [2, 8],
    [7, 5]
])
print((A @ B)[0, 0])
print((A @ B)[0, 1])
print((A @ B)[1, 0])
print((A @ B)[1, 1])
print(A @ B)
