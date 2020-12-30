from sympy import *

A = Matrix([
    [1, 2, 3, 4, 5, 6, 7],
    [8, 9, 10, 11, 12, 13, 14],
    [15, 16, 17, 18, 19, 20, 21],
    [22, 23, 24, 25, 26, 27, 28],
    [29, 30, 31, 32, 33, 34, 35]
])
R, _ = A.rref()
pprint(R)
s, t, p, q, r = symbols('s t p q r')
a1 = s + 2 * t + 3 * p + 4 * q + 5 * r
a2 = -2 * s - 3 * t - 4 * p - 5 * q - 6 * r
a3 = s
a4 = t
a5 = p
a6 = q
a7 = r
a = Matrix([[a1, a2, a3, a4, a5, a6, a7]]).T
pprint(a)
# gather the coefficient for each variable into one vector each
# so that we have Ax=b where the vectors make up A, x are s, t, p, q, and r,
# and b is the zero vector
v1 = Matrix([1, -2, 1, 0, 0, 0, 0])
v2 = Matrix([2, -3, 0, 1, 0, 0, 0])
v3 = Matrix([3, -4, 0, 0, 1, 0, 0])
v4 = Matrix([4, -5, 0, 0, 0, 1, 0])
v5 = Matrix([5, -6, 0, 0, 0, 0, 1])
pprint([v1, v2, v3, v4, v5])
pprint(A.nullspace())
# manually doing this is accident prone
