import numpy as np

A = np.array([
    [1, 3, 6],
    [4, 7, -1],
    [5, 3, 2]
])
B = np.array([
    [-1, 3, -5, -6],
    [2, 1, -7, 2],
    [6, 4, 9, 1]
])
result = A @ B
print('(AB)12', result[0, 1])
print('(AB)23', result[1, 2])
print('(AB)31', result[2, 0])
# print('(AB)43', result[3, 2])  # index out of range
print('(AB)34', result[2, 3])
