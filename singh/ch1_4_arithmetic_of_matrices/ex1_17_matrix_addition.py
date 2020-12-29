import numpy as np

# a
m1 = np.array([
    [1, 2],
    [3, 4]
])
m2 = np.array([
    [5, 6],
    [7, 8]
])
print('a')
print(m1 + m2)

# b
m1 = np.array([
    [1, 2, 5, 6, 1],
    [7, 9, 11, 6, 3]
])
m2 = np.array([
    [9, 8, 5, 7, 6],
    [2, 13, 7, 2, 3]
])
print('b')
print(m1 - m2)

# c
m1 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
m2 = np.array([
    [1, 1, 1],
    [3, 3, 3],
    [4, 4, 4]
])
print('c')
print(m1 - m2)

# d
# this cannot be done, gives this error:
# ValueError: operands could not be broadcast together with shapes (2,2) (2,3)
#
# m1 = np.array([
#     [2, 3],
#     [5, 4]
# ])
# m2 = np.array([
#     [1, 2, 4],
#     [8, 4, 0]
# ])
# print('d')
# print(m1 - m2)
