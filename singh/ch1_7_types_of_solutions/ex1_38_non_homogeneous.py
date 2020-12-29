import numpy as np

m = np.array([
    [1, -1, 2, 0, 3, 1],
    [-1, 1, 0, 2, -5, 5],
    [1, -1, 4, 2, 4, 13],
    [-2, 2, -5, -1, 3, -1]
], dtype='float')
m[1] += m[0]
m[2] -= m[0]
m[2] -= m[1]
m[3] += 2 * m[0]
m[3] += (1 / 2) * m[1]
m[3] -= (8 / 3) * m[2]
m[2] /= 3
m[1] /= 2
# Book ends here, but can I do more?
m[1] += m[2]
print(m)
# Seems like it, and get the same final answer after solving for each row
