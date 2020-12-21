import numpy as np

m = np.array([
    [1, 2, 1, 1],
    [2, 2, 3, 2],
    [5, 8, 2, 4]
])
m = m.astype(float)
print(m)

m[1] = m[1] - 2 * m[0]
print(m)

m[2] = m[2] - 5 * m[0]
print(m)

m[2] = m[2] - m[1]
print(m)

m[2] = m[2] / -4
print(m)

m[1] = m[1] - m[2]
print(m)

m[1] = m[1] / -2
print(m)

m[0] = m[0] - m[2]
print(m)

m[0] = m[0] - m[1] * 2
print(m)

print('result:', m[:, 3])
# 1/2, 1/8, 1/4
