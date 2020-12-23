import numpy as np

m = np.array([
    [5, 2, 1],
    [8, 4, 0]
])
m = m.astype(float)
m[1] -= (m[0] * (8/5))
m[1] /= 0.8
m[0] -= m[1] * 2
m[0] /= 5
m = m.astype(int)
print('(i) yes:', m[:, 2])

m = np.array([
    [5, 2, 0],
    [8, 4, 1]
])
m = m.astype(float)
m[1] -= m[0] * (8/5)
m[1] /= 0.8
m[0] -= m[1] * 2
m[0] /= 5
m = m.astype(int)
print('(ii) yes:', m[:, 2])

m = np.array([
    [1, 0, 1],
    [0, 1, 2],
    [0, 0, 3]  # sus
])
print('(iii) no, cannot get that 3 when *ing u and v by any value of x and y')

m = np.array([
    [4, 1, 1],
    [8, 2, 2],
    [0, -3/7, 3]
])
m[1] -= m[0] * 2
m[[2, 1]] = m[[1, 2]]
m[1] /= m[1, 1]
m[0] -= m[1]
m[0] /= 4
print('(iiii) yes:', m[:, 2])
