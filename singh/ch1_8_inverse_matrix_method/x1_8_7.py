from sympy import *

# p = Ap + d
# p - Ap = d
# Ip - Ap = d
# (I - A)p = d
# ^^^^^^^---------- this will be the A in Ax=b

m = Matrix([
    [0.25, 0.15, 0.1],
    [0.4, 0.15, 0.2],
    [0.15, 0.2, 0.2]
])
A = eye(3) - m
d = Matrix([[100, 100, 100]]).T
Ai = A.inv()
p = Ai @ d
pprint(p)
