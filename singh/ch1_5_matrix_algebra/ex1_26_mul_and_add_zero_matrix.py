import numpy as np

A = np.array([
    [1, 2],
    [9, 7]
])
B = np.array([
    [2, 3, -1],
    [5, -7, 6]
])
C = np.array([[2, -5, 9]]).T

print('a')
print((A @ B) @ C)
print('b')
print(A @ (B @ C))
# print('c')
# print(A @ (B + C))  # B cannot be added to C
# print('d')
# print(A @ B + A @ C)  # A cannot be multiplied with C
# print('e')
# print((B + C) @ A)  # B cannot be added to C
print('f')
print(A @ np.zeros((2, 2)))
print('g')
print(B @ np.zeros((3, 3)))
print('h')
print(C @ np.zeros((1, 3)))  # but the book's answer is just a 0 scalar?
