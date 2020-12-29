import numpy as np

u = np.array([1, 2, 3])
v = np.array([1, 1, 1])
c = 1

n = np.linalg.norm(u @ v + c)
d = np.linalg.norm(v)
print(n / d)
# This is the shortest distance between the plane x + y + z = -1 and vector (1 2 3)
