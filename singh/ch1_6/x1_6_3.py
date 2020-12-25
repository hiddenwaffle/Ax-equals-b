import numpy as np

u = np.array([[1, 2, 3]]).T
v = np.array([[4, 5, 6]]).T

print('a')
print(u.T @ v)
print('b')
print(v.T @ u)
print('c')

# To get @ to do the dot product I used vectors instead of matrices...
u = np.array([1, 2, 3])
v = np.array([4, 5, 6])
print(u @ v)
# ...is this the right way to interpret this?
