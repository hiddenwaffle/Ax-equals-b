import numpy as np
from numpy.linalg import matrix_power

m = np.array([
    [1, 0],
    [0, 1]
])
print('a')
print(matrix_power(m, 2))
print(matrix_power(m, 3))
print(matrix_power(m, 4))
# always m (identity matrix I)

m = np.array([
    [0, 1],
    [-1, 0]
])
print('b')
print(matrix_power(m, 2))
print(matrix_power(m, 3))
print(matrix_power(m, 4))
# the fourth power settles into I

m = np.array([
    [1/2, 1/2],
    [1/2, 1/2]
])
print('c')
print(matrix_power(m, 2))
print(matrix_power(m, 3))
print(matrix_power(m, 4))
# always m, this is a Markov matrix (columns add up to 1)
