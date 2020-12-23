import numpy as np

A = np.array([
    [1, -1, 7],
    [2, 9, 6]
])
B = np.array([
    [5, 1, 4],
    [8, 2, 7],
    [1, 4, 9]
])
C = np.array([2, 4, 7])
D = np.array([
    [7, 9, 4],
    [1, 3, -5],
    [2, -1, -3]
])

print('a', "\n", A - A)
print('b', "\n", 3 * A - 2 * A)
print('c', "\n", B @ C)
print('e', "\n", B + D)
print('f', "\n", D + B)
print('h', "\n", (1/2) * C)
print('i', "\n", B @ D)
print('j', "\n", D @ B)
print('k', "\n", B @ D - D @ B)

# d, g, and l are impossible but numpy does them anyway
print('d', "\n", C @ B)  # numpy used C as-is (a row vector)
print('g', "\n", A - C)  # numpy subtracted C from each row of A
print('l', "\n", C @ D)  # numpy used C as-is (a row vector)
