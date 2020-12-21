import numpy as np

m = np.array([
    [2, 1, -1, 2],
    [4, 3, 2, -3],
    [6, -5, 3, -14]
])
m = m.astype(float)
print(m)

m[1] -= m[0] * 2
print(m)

m[2] -= m[0] * 3
print(m)

m[2] += m[1] * 8
print(m)

m[2] /= 38
print(m)

m[1] -= m[2] * 4
print(m)

m[0] += m[2]
print(m)

m[0] -= m[1]
print(m)

m[0] /= 2
print(m)

print('final:', m[:, 3])
