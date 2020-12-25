import numpy as np

print('a')
A = np.array([
    [1, 2],
    [3, 4]
])
print(A.T)

print('b')
A = np.array([
    [1, 2, 3],
    [-1, -2, -3]
])
print(A.T)

print('c')
A = np.array([[-1, 5, 9, 100]])
print(A.T)

# skip d

print('e')
A = np.zeros((3, 2))
print(A.T)

print('f')
A = np.array([
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [0, 0, 0, 0]
])
print(A.T)
