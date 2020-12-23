import numpy as np

m = np.array([
    [1, 1, 1, -2],
    [2, -1, -1, -4],
    [4, 2, -3, -3]
])
m = m.astype(float)
print(m)

m[1] -= m[0] * 2
print(m)

m[2] -= m[0] * 4
print(m)

m[2] -= m[1] * (2/3)
print(m)

m[2] /= -5
print(m)

m[1] -= m[2] * -3
print(m)

m[1] /= -3
print(m)

m[0] -= m[2]
print(m)

m[0] -= m[1]
print(m)

print('final:', m[:, 3])
