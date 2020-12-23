import numpy as np
from numpy.linalg import matrix_power

A = np.array([
    [1, -1],
    [1, -1]
])
print(A @ A)
print(matrix_power(A, 2))

# It zeroed out the matrix, so any higher powers will also be zeroed
