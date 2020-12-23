import numpy as np

u = np.array([1, 0, 0])
v = np.array([0, 1, 0])
w = np.array([0, 0, 1])
x = np.array([100, 1000, 10000])

print(x[0] * u + x[1] * v + x[2] * w)
print(x)
