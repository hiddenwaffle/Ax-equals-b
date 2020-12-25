import numpy as np
from numpy.linalg import matrix_power

A = np.array([
    [-1, 4, 8],
    [-9, 1, 2]
])
B = np.array([
    [5, 8],
    [0, -6],
    [5, 6]
])
C = np.array([
    [-4, 1],
    [6, 5]
])
D = np.array([
    [-6, 3, 1],
    [8, 9, -2],
    [6, -1, 5]
])
print('a')
print((A @ B).T)
print('b')
print((B @ C).T)
print('c')
print(C - C.T)
print('d')
print(D - D.T)
print('e')
print(D.T.T)
print('f')
print((2 * C).T)
print('g')
print(A.T + B)
print('h')
print(A + B.T)
print('i')
print((A.T + B).T)
print('j')
print((2 * A.T - 5 * B).T)
print('k')
print((-D).T)
print('l')
print(-D.T)
print('m')
print(matrix_power(C, 2).T)
print('n')
print(matrix_power(C.T, 2))
