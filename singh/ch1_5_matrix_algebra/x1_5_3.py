import numpy as np

A = np.array([
    [1, 5, -2],
    [3, 7, -9]
])
B = np.array([
    [-1, 0, 7],
    [-3, 2, 1],
    [-4, 1, 6]
])
C = np.array([
    [7, 8, 1],
    [-8, 6, -6],
    [6, -3, 5]
])

print('a')
print(A @ B)
# print('b')
# print(B @ A)  # Mismatch number of rows and columns
print('c')
print(A @ (B + C))
print('d')
print(A @ B + A @ C)
# print('e')
# print((B + C) @ A)  # Mismatch number of rows and columns
# print('f')
# print(B @ A + C @ A)   # Again, cannot multiply B and A (see part b)
print('g')
print(C @ np.zeros((3, 3)))
print('h')
print(B @ np.zeros((3, 3)) + C @ np.zeros((3, 3)))
print('i')
print(np.zeros((3, 3)) @ B + np.zeros((3, 3)) @ C)
# print('j')
# print((A + B) @ C)  # Cannot add A and B
# print('k')
# print(A @ C + B @ C)  # Cannot multiply A and C
