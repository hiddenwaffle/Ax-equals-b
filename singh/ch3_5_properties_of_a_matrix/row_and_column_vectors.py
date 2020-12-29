import numpy as np

A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print('row vectors')
for rv in A:
    print(rv)
print('column vectors')
for cv in A.T:
    print(cv)

B = np.array([
    [-3, 6],
    [-5, 2],
    [-2, 7]
])
print('row vectors')
for rv in B:
    print(rv)
print('column vectors')
for cv in B.T:
    print(cv)
