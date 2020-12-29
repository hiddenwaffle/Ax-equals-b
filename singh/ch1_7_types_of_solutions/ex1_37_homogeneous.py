import numpy as np

m = np.array([
    [-1, 2, 3, 0],
    [1, -4, -13, 0],
    [-3, 5, 4, 0]
], dtype='float')
m[1] += m[0]
m[2] -= 3 * m[0]
m[2] -= (1 / 2) * m[1]
print(m)

# From the second row:
# -2y - 10z = 0
# -2y = 10z
# y = -5z

# From the first row:
# -x + 2y + 3z = 0
# -x + 2(-5z) + 3z = 0
# -x -10z + 3z = 0
# -x -7z = 0
# -x = 7z
# x = -7z

# Spot checking t = 1:
# -x + 2y + 3z = 0
# -(-7) + 2(-5) + 3 = 0
# 7 - 10 + 3 = 0
