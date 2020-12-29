import numpy as np
from numpy.linalg import inv

A = np.zeros((2, 2))
B = np.ones((2, 2))
C = np.array([
    [1, 3],
    [2, 6]
])
# All of these raise an error: "Singular matrix"
# inv(A)
# inv(B)
# inv(C)
