import numpy as np

u = np.array([2, 3, -1])
v = np.array([5, 1, -2])

print('a', u @ v)
print('b', v @ u)
print('c', u @ u)
print('d', v @ v)
print('e', np.linalg.norm(u) ** 2)
print('f', np.linalg.norm(v) ** 2)
print('g', np.linalg.norm(u))
print('h', np.linalg.norm(v))
print('i', np.linalg.norm(u + v) ** 2)
print('j', np.linalg.norm(u - v))
