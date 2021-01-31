from sympy import *

A = Matrix([
    [1, 4],
    [2, 3]
])
# Extract the eigenvectors A into their own matrix P
ev1, ev2 = (A.eigenvects())
_, _, ev1 = ev1
ev1 = ev1[0]
_, _, ev2 = ev2
ev2 = ev2[0]
P = Matrix([
    [ev1, ev2]
])
print('P')
pprint(P)
# Extract the eigenvalues into their own matrix D
evals = list(A.eigenvals().keys())
D = Matrix([
    [evals[1], 0],  # evals[1] lines up with ev1
    [0, evals[0]]  # evals[0] lines up with ev2
])
print('D')
pprint(D)
print('PD = AP')
pprint(P * D)
pprint(A * P)
