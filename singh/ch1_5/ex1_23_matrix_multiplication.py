import numpy as np

A = np.array([
    [-1, 3, 4],
    [9, 6, 1]
])
B = np.array([
    [1, 5, 8],
    [-2, 3, 2]
])
c = -2
k = 5

print('a')
print((c + k) * B)
print('b')
print(c * B + k * B)
print('c')
print(-10 * A)
print('d')
print(c * (k * A))
print('e (then * x)')
print(k * (A + B))
print('---')

m = np.array([
    [14, 14, 28],
    [-77, -21, 7]
], dtype='float')  # leave off the 0s, which is the zero vector
m_original = m.copy()
m /= 7  # factor out a 7, which is (c - k)
m -= A  # subtracting out B leaves -A
print(m)
print((c - k) * (A - B))  # reconstructing m in terms of A, B, c, and k
# use this matrix with x and 0 to complete the problem
