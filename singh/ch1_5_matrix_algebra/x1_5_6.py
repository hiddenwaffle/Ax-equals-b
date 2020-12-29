import numpy as np

A = np.array([
    [-1, 3, 5],
    [4, 1, -7]
])
B = np.array([
    [1, -3, -5],
    [-4, -1, 7]
])
c = -9
k = 8

print('a')
print((c * k) * A)
print('b')
print(c * (k * A))
print('c')
print(k * (A + B))
print('d')
print(k * A + k * B)
print('e')
print((c + k) * A)
print('f')
print(c * A + k * A)
print('g')
print((c + k) * B)
print('h')
print(c * B + k * B)
