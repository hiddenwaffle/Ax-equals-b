import numpy as np

u = np.array([-9, 2, 4])
v = np.array([-2, 1, 3])
w = np.array([1, -2, 5])

print('a', u + v + w)
print('b', u - v - w)
print('c', 2 * u + v - w)
print('d', -2 * u + 3 * v + 5 * w)
