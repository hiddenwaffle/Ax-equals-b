import numpy as np

# a
m1 = np.array([3, 4])
m2 = np.array([
    [2, 3],
    [-1, 5]
])
print('a')
print(m1 @ m2)

# b
m1 = np.array([
    [2, 3, 6],
    [1, 5, 7]
])
m2 = np.array([
    [3, 7],
    [4, 2],
    [1, 3]
])
print('b')
print(m1 @ m2)

# c cannot be computed
