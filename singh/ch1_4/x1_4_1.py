import numpy as np

A = np.array([
    [1, 2],
    [3, -1]
])
B = np.array([
    [6, -1],
    [5, 3]
])
C = np.array([
    [-1],
    [1]
])

print('a', "\n", A + B)
print('b', "\n", B + A)
print('c', "\n", B + B + B)
print('d', "\n", 3 * B)
print('e', "\n", 3 * A + 2 * B)
print('h', "\n", A @ C)
print('i', "\n", B @ C)
print('k', "\n", 3 * A @ C - 2 * B @ C)

# f, g, and j should not be evaluatable but numpy does them anyway
# print('f', "\n", A + C)  # numpy added C to both columns of A
# print('g', "\n", B + C)  # numpy added C to both columns of B
# print('j', "\n", 5 * A - 7 * B @ C)  # numpy subtracted 7 * B @ C from each column of 5 * A
