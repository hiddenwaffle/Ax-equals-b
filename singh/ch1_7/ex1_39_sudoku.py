import numpy as np
import sympy

m = np.array([
    [1, 1, 1, 0, 0, 0, 15],
    [0, 0, 0, 1, 1, 1, 6],
    [1, 0, 0, 1, 0, 0, 8],
    [0, 1, 0, 0, 1, 0, 7],
    [0, 0, 1, 0, 0, 1, 6]
])

m, pivots = sympy.Matrix(m).rref()
m = np.array(m, dtype=float)
print(m)
print(pivots)
