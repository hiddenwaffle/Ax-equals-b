import numpy as np
from numpy.linalg import inv

A = np.array([
    [1, 2, 0],
    [2, 5, -1],
    [4, 10, -1]
])
b = np.array([
    [1],
    [2],
    [3]
])
Ai = inv(A)
print(Ai @ b)
