import numpy as np

A = np.array([
    [3, -4, 1],
    [5, 2, 6]
])
B = np.array([
    [-2, 7, 5],
    [1, 3, -9]
])
print('a')
print(A.T.T)
print('b')
print((2 * A).T - (3 * B).T)
print('c')
print((A + B).T)
print('d')
print(A.T + B.T)
# print('e')
# print((A @ B).T)  # Cannot be multiplied
