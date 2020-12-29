import numpy as np

m = np.array([
    [1, 1, 2, 3],
    [-1, 3, -5, 7],
    [2, -2, 7, 1]
])
m[1] += m[0]
m[2] -= 2 * m[0]
m[2] += m[1]  # reveals inconsistency; 0 cannot equal 5
print(m)
