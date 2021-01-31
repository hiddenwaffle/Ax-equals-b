from sympy import *

A = Matrix([
    [1, 0],
    [1, 2]
])
P = Matrix([
    [0, -1],
    [1, 1]
])
Pi = P.inv()
pprint([Pi, A, P])
B = Pi * A * P
pprint(B)
# B is "similar" to A

# A and B have the same eigenvalues
print(A.eigenvals(), (B.eigenvals()))
