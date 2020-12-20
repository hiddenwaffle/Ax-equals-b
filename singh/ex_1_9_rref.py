from fractions import Fraction
import numpy as np
from util.frac import pretty_fractions

# Avoid back substitution by carrying out Gauss-Jordan elimination

pretty_fractions()

a1 = np.array([
    [1, 5, -3, -9],
    [0, -13, 5, 37],
    [0, 0, 5, -15]
])

num_rows, _ = a1.shape
print(a1[num_rows - 1])
