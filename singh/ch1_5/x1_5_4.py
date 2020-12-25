import numpy as np

A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
I3 = np.identity(3)
print(A @ I3)
print(I3 @ A)
# identity matrix works on either side, same outcome
# AI = IA = A
