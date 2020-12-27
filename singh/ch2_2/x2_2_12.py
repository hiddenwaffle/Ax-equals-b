import numpy as np

print('a')
u = np.array([1, 1])
v = np.array([1, -1])
c = 1
n = np.linalg.norm(u @ v + c)
d = np.linalg.norm(v)
print(n / d)

print('b')
u = np.array([0.5, 2])
v = np.array([2, -1])
c = -1
n = np.linalg.norm(u @ v + c)
d = np.linalg.norm(v)
print(n / d)

print('c')
u = np.array([-1, -3, 3])
v = np.array([2, 1, -1])
c = -7
n = np.linalg.norm(u @ v + c)
d = np.linalg.norm(v)
print(n / d)

print('d')
u = np.array([1, 2, 3, 4])
v = np.array([1, 2, 1, 1])
c = -10
n = np.linalg.norm(u @ v + c)
d = np.linalg.norm(v)
print(n / d)
