from sympy import *

Q = (1 / sqrt(2)) * Matrix([
    [1, 1],
    [1, -1]
])
u = Matrix([[1, 2]]).T
w = Matrix([[3, 1]]).T

print('i')
pprint((Q * u).T * (Q * w))  # Q * u and Q * w return vectors, so transpose
print('ii')
pprint(u.T * w)  # ditto
# iii - They are equal
