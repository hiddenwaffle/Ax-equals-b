import numpy as np

# a
A = np.array([
    [2, 3],
    [-1, 5]
])
x = np.array([
    [2],
    [1]
])
print('a')
print(A @ x)

# b
A = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])
x = np.array([
    [3],
    [4]
])
print('b')
print(A @ x)

# c
A = np.array([
    [1, 0]
])
x = np.array([
    [3],
    [4]
])
print('c')
print(A @ x)
