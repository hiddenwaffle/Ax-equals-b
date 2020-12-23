import numpy as np

m = np.array([
    [1, 1, 2, 9],
    [4, 4, -3, 3],
    [5, 1, 2, 13]
])
m = m.astype(float)
print(m)

m[1] -= m[0] * 4
print(m)

m[2] -= m[0] * 5
print(m)

# Swap two rows: https://stackoverflow.com/a/54069951
m[[1, 2], :] = m[[2, 1], :]
print(m)

m[2] /= -11
print(m)

m[1] -= m[2] * -8
print(m)

m[1] /= -4
print(m)

m[0] -= m[2] * 2
print(m)

m[0] -= m[1]
print(m)

print('final:', m[:, 3])
