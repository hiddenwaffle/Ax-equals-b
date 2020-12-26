import numpy as np
from sympy import *

A = np.array([
    [1, -2, 3, 5],
    [2, 5, 6, 9],
    [-3, 1, 2, 3],
    [1, 13, -30, -49]
])
I = np.identity(4)
A = np.hstack((A, I))
A = Matrix(A)
A, p = A.rref()
A = np.array(A, dtype='float')
np.set_printoptions(precision=2)
print(A)  # row of zeros on the left side of the augmented matrix
print(p)  # missing 3, it skipped to 4
# A is non-invertible
# Either Ax = b has an infinite # of solutions, or no solution
# In either case, there is no unique solution
