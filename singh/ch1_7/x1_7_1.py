import numpy as np
from sympy import Matrix

print('a')
m = Matrix([
    [1, 3, 2, 5],
    [2, -1, -1, 1],
    [-1, 2, 1, 3]
])
m, p = m.rref()
m = np.array(m)
print(p, m[:, 3])

print('b')
m = Matrix([
    [-1, 1, 1, 0],
    [3, -2, 5, 0],
    [4, -1, -2, 0]
])
m, p = m.rref()
m = np.array(m)
print(p, m[:, 3])

print('c')
m, p = Matrix([
    [-1, 1, 1, 2],
    [2, 2, 3, 5],
    [6, 6, 9, 7]
]).rref()
m = np.array(m)
print(m)  # notice 3rd row is all zeros except the constant
print(p, m[:, 3])  # pivot includes a 3, which is on the right side, means no solution?

print('d')
m, p = Matrix([
    [1, 1, -1, 2],
    [1, 2, 1, 4],
    [3, 3, -3, 6]
]).rref()
m = np.array(m)
print(m)  # notice 3rd row is all zeros, including the constant
print(p, m[:, 3])  # has only 2 pivot entries (0, 1), means infinitely many solutions?
# y + 2z = 2    => y = 2 - 2z
# x - 3z = 0    => x = 3z
# Therefore: x = 3t, y = 2 - 2t, z = t

print('e')
m, p = Matrix([
    [3, -3, -1, 2, 0],
    [6, -7, 1, 1, 0],
    [1, -1, -2, -1, 0],
    [2, -2, 6, 8, 0]
]).rref()
m = np.array(m)
print(m)  # notice 3rd row is all zeros, including the constant
print(p, m[:, 4])  # has only 3 pivot entries (0, 1, 2), means infinitely many solutions
# x + 7w = 0    => x = -7w
# y + 6w = 0    => y = -6w
# z + w = 0     => z = -w
# w = t
# Therefore: x = -7t, y = -6t, z = -t, w = t

print('f')
m, p = Matrix([
    [2, 3, 5, 2, 6],
    [2, 3, 2, 2, 7],
    [8, 12, 20, 8, 24],
    [1, 2, 4, 5, 6]
]).rref()
m = np.array(m)
print(m)  # 4th row has all zeros, including the constant
print(p, m[:, 4])  # has only 3 pivot entries (0, 1, 2)
# x - 11w = -20/3   => x = 11w - 20/3
# y + 8w = 7        => y = 7 - 8w
# z = -1/3
# Therefore, x = 11t - 20/3, y = 7 - 8t, z = -1/3, w = t

print('g (as written)')
m, p = Matrix([
    [0, -10, 0, 38, 6],
    [5, 6, -8, 4, 3],
    [10, 7, 3, 8, 9]
]).rref()
m = np.array(m)
print(m)  # 3 leading ones but 4 variables
print(p, m[:, 4])  # pivot (0, 1, 2) corresponds to (x, y, w), z is free
# x + 94/25z = 33/25    => x = 33/25 - 94/25z
# y - 19/5z = -3/5      => y = 19/5z - 3/5
# w - z = 0             => w = z
# NOTE: The book answer doesn't look right?
#       It looks like they put 38 in for w instead of z on the first row

print('g (solution from the book)')
m, p = Matrix([
    [0, -10, 38, 0, 6],
    [5, 6, -8, 4, 3],
    [10, 7, 3, 8, 9]
]).rref()
m = np.array(m)
print(m)  # Notice unlike previous, this has a row of zeros
print(p, m[:, 4])  # Also this has only 2 pivot out of 4 variables, so 2 free
# x + 74/25w + 4/5z = 33/25     => x = 33/25 - 74/25w - 4/5z
#                               => x = 33/25 - 74/25w - 20/25z
#                               => x = (1/25)(33 - 74w - 20z)
# y - 19/5w = -3/5      => y = 19/5w - 3/5
#                       => y = (1/5)(19w - 3)
# and then replace w and z with parameter variable names,
# and set w and z to them

print('h')
m, p = Matrix([
    [0, -1, 0, 0, 5, 3],
    [3, -4, 1, 6, 7, 5],
    [15, -20, 2, 30, 3, -1],
    [12, -16, 7, 24, 60, 10]
]).rref()
m = np.array(m)
print(m)  # bottom row is inconsistent, 0 cannot equal 1
print(p, m[:, 5])  # notice that 5 is one of the pivot variables, means inconsistency

print('i')
m, p = Matrix([
    [0, -1, 0, 0, 5, 3],
    [3, -4, 1, 6, 7, 5],
    [15, -20, 2, 30, 3, -1],
    [12, -16, 7, 24, 60, 46]
]).rref()
m = np.array(m)
print(m)
print(p)
# x + 2w - 71/9u = -47/9    => x = 71/9u - 2w - 47/9
# y - 5z = -3               => y = 5z - 3
# z + 32/3u = 26/3          => z = 26/3 - 32/3u
# and so on

print('j')
m, p = Matrix([
    [2, -1, 3, 5, 5, 1],
    [1, 7, 6, -11, 7, -8],
    [1, -2, 6, 4, 1, 5],
    [2, -6, 0, 14, 2, 20 / 3]
]).rref()
m = np.array(m)
print(m)
print(p)
# x + 2w + 3u = - 1
# y + -5/3w + 2/3u = -13/9
# z + -2/9w -1/9u = 14/27
# and so on
