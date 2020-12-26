from sympy import *

print('a')
A = Matrix([
    [1, 2],
    [-1, 4]
])
Ai = A.inv()
pprint(Ai)

print('b')
B = Matrix([
    [2, -5],
    [-6, 1]
])
Bi = B.inv()
pprint(Bi)

print('c')
C = Matrix([
    [1, 0, 2],
    [2, 3, 1],
    [3, 6, 0]
])
# Ci = C.inv()  # Matrix det == 0; not invertible.
# pprint(Ci)

print('d')
D = Matrix([
    [1, -1, 1],
    [1, 0, -1],
    [0, 0, -1]
])
Di = D.inv()
pprint(Di)

print('e')
E = Matrix([
    [2, -1, 0],
    [-1, 2, -1],
    [0, -1, 2]
])
Ei = E.inv()
pprint(Ei)

print('f')
F = Matrix([
    [1, 3, 4],
    [-1, 1, 1],
    [2, 1, -2]
])
Fi = F.inv()
pprint(Fi)

print('g')
G = Matrix([
    [-2, 5, 3, 1],
    [-9, 2, -5, 6],
    [2, 4, 8, 16],
    [4, 8, 16, 32]
])
# Gi = G.inv()  # Matrix det == 0; not invertible.
# pprint(Gi)

print('h')
H = Matrix([
    [1, 2, -2, 3],
    [-2, 1, -5, -6],
    [-5, -10, 9, -15],
    [-6, -12, 27, -18]
])
# Hi = H.inv()  # Matrix det == 0; not invertible.
# pprint(Hi)

print('j')
J = Matrix([
    [1, 2, -2, 3],
    [-2, 1, -5, -6],
    [-5, -10, 9, -15],
    [-6, -12, 12, -19]
])
Ji = J.inv()
pprint(Ji)
