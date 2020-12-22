import numpy as np

u = np.array([2, 3, -1])
v = np.array([5, 1, -2])

print('a', np.dot(u, v))
print('b', np.dot(v, u))
print('c', np.dot(u, u))
print('d', np.dot(v, v))
