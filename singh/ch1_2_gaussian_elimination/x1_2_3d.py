import numpy as np

m = np.array([
    [-2, 3, -2, 8],
    [-1, 2, -10, 0],
    [5, -7, 4, -20]
])
m = m.astype(float)
print(m)

m[[0, 1], :] = m[[1, 0], :]
print(m)

m[1] -= m[0] * 2
print(m)

m[2] += m[0] * 5
print(m)

m[2] += m[1] * 3
print(m)

m[2] /= 8
print(m)

m[1] -= m[2] * 18
print(m)

m[1] /= -1
print(m)

m[0] += m[2] * 10
print(m)

m[0] -= m[1] * 2
print(m)

m[0] /= -1
print(m)

print('final:', m[:, 3])
