import numpy as np


# Use Gaussian elimination to get:
# a = [
#     *, *, *, *,
#     0, *, *, *,
#     0, 0, A, B
# ]
# where A, B, and * are real numbers

a1 = np.array([
    [1, -3, 5, -9],
    [2, -1, -3, 19],
    [3, 1, 4, -13]
])
print(a1)
print('---')

a2 = np.array([
    a1[0],
    a1[1] - a1[1, 0] * a1[0],
    a1[2]
])
print(a2)
print('---')

a3 = np.array([
    a2[0],
    a2[1],
    a2[2] - a2[2, 0] * a2[0]
])
print(a3)
print('---')

final = np.array([
    a3[0],
    a3[1],
    a3[2] - (a3[2, 1] / a3[1, 1]) * a3[1]
])
print(final)
print('---')

# Use backsubstitution to solve
z = final[2, 3] / final[2, 2]
y = (final[1, 3] - final[1, 2] * z) / final[1, 1]
x = (final[0, 3] - final[0, 1] * y - final[0, 2] * z) / final[0, 0]
print('x:', x, 'y:', y, 'z:', z)
