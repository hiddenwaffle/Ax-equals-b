import numpy as np
from sympy import Matrix

m = Matrix([
    [2, -4, 4, 0.077, 3.86],
    [0, -2, 2, -0.056, -3.47],
    [2, -2, 0, 0, 0]
])
m, p = m.rref()
m = np.array(m)
print(m)
print(p)
# x + 0.0945t = 5.4     => x = 5.4 - 0.0945t
# y + 0.0945t = 5.4     => y = 5.4 - 0.0945t
# z + 0.0665t = 3.665   => z = 3.665 - 0.0665t
