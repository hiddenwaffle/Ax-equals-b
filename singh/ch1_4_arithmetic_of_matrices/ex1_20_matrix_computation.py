import numpy as np

a = np.array([
    [1, 2, 5],
    [4, 6, 9]
])
b = np.array([
    [2, 5, 6],
    [1, 7, 2],
    [9, 6, 1]
])
c = np.array([
    [5, 4, 9],
    [7, 4, 0],
    [6, 9, 8]
])

print('a', "\n", b + c)
# print('b', "\n", a + b)  # cannot, different shapes
print('c', "\n", 3 * b + 2 * c)
print('d', "\n", a @ b)
# print('e', "\n", b @ a)  # cannot, 2 rows vs 3 columns
