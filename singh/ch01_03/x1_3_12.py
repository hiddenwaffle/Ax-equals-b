import numpy as np

m = np.array([
    [1, 0, -2, 5],
    [2, 1, 0, 3],
    [0, -1, 6, 17]
])
m = m.astype(float)
print(m)

m[1] -= m[0] * 2
print(m)

m[2] += m[1]
print(m)

m[2] /= 10
print(m)

m[1] -= m[2] * 4
print(m)

m[0] += m[2] * 2
print(m)

print('x y z =', m[:, 3])
