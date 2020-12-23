import numpy as np

A = np.array([
    [1, 2, 0],
    [3, 5, 0]
])
A[1] -= A[0] * 3
A[1] *= -1
A[0] -= A[1] * 2
print('a', A[:, 2])

A = np.array([
    [2, 7, 0],
    [3, 15, 0]
])
A = A.astype(float)
A[1] -= A[0] * (3/2)
A[1] /= 4.5
A[0] -= A[1] * 7
A[0] /= 2
print('b', A[:, 2])

A = np.array([
    [1, 4, 0],
    [3, 12, 0]
])
A[1] -= A[0] * 3
print('c', "\n", A)  # Cannot achieve rref, bottom row went to all zeros
# the remaining row says x + 4y = 0, so x and y can be "any real number"
