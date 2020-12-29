import numpy as np

m = np.array([
    [3, -1, 7, 9],
    [5, 3, 2, 10],
    [9, 2, -5, 6]
])
m = m.astype(float)
print(m)

m[1] -= m[0] * (5 / 3)
print(m)

m[2] -= m[0] * 3
print(m)

m[2] -= m[1] * (5 / m[1, 1])
print(m)

m[2] /= m[2, 2]
print(m)

m[1] -= m[2] * m[1, 2]
print(m)

m[1] /= m[1, 1]
print(m)

m[0] -= m[2] * 7
print(m)

m[0] += m[1]
print(m)

m[0] /= 3
print(m)

print('final:', m[:, 3])
# should all equal 1
