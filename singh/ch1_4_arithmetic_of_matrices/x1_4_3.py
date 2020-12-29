import numpy as np

m1 = np.array([
    [2, 4],
    [3, 9]
])
m2 = np.array([
    [1, 0],
    [0, 1]
])
print('a', "\n", m1 @ m2)

m1 = np.array([
    [6, 7],
    [2, 3]
])
print('b', "\n", m1 @ m2)

m1 = np.array([
    [555, 666],
    [777, 888]
])
print('c', "\n", m1 @ m2)

m1 = np.array([
    [2, 3, 6],
    [1, 4, 5],
    [0, 9, 7]
])
m2 = np.array([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
])
print('d', "\n", m1 @ m2)
