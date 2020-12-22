import numpy as np

u = np.array([-3, 1])
v = np.array([1, 3])

print('a', u + v)
print('b', 3 * u + 2 * v)
print('c', u - u)

m = np.array([
    [-3, 1, 0],
    [1, 3, 0]
])
m = m.astype(float)
m[[0, 1], :] = m[[1, 0], :]
m[1] += m[0] * 3
m[1] /= 10
m[0] -= m[1] * 3

print('0u + 0v =', m[:, 2])
