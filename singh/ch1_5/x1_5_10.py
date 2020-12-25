import numpy as np
from numpy.linalg import matrix_power

T = np.array([
    [0.6, 0.7],
    [0.4, 0.3]
])
p = np.array([
    [0.5],
    [0.5]
])
print(matrix_power(T, 1) @ p)
print(matrix_power(T, 2) @ p)
print(matrix_power(T, 10) @ p)
print(matrix_power(T, 100) @ p)
print(matrix_power(T, 100000) @ p)
# the fractions become more and more precise
