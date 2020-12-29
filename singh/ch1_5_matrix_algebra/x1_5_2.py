import numpy as np

A = np.array([
    [5, -1, -2],
    [1, -3, 2]
])
print('a')
B = -A
print(B)
print('b')
C = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print(A + (-C))
print(A - C)
print('c')
print(A - B - C)
print(A - (B - C))
