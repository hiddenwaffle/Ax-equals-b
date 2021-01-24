from itertools import permutations
from sympy import *

print('a')
u = Matrix([[5, 0, 0]]).T
v = Matrix([[0, 1, 0]]).T
w = Matrix([[0, 0, 10]]).T
B = [u, v, w]
for a, b in permutations(B, 2):
    pprint(a.T * b)
# all zeros

print('b')
u = Matrix([[0, 0, 0]]).T
v = Matrix([[1, 1, -1]]).T
w = Matrix([[-3, 10, 7]]).T
B = [u, v, w]
for a, b in permutations(B, 2):
    pprint(a.T * b)
# all zeros
