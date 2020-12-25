import numpy as np
from numpy.linalg import inv

A = np.array([
    [3, 2],
    [6, 4]
])
# Ai = inv(A)  # Error: "numpy.linalg.LinAlgError: Singular matrix"
