from sympy import *

print('a')
R, p = Matrix([
    [1, 2],
    [3, 4]
]).T.rref()
pprint(R)
print('rank', len(p))

print('b')
R, p = Matrix([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]).T.rref()
pprint(R)
print('rank', len(p))

print('c')
R, p = Matrix([
    [1, 2],
    [3, 4],
    [5, 6]
]).T.rref()
pprint(R)
print('rank', len(p))

print('d')
R, p = Matrix([
    [1, 2, 3],
    [4, 5, 6]
]).T.rref()
pprint(R)
print('rank', len(p))

print('e')
R, p = Matrix([
    [-1, 2, 5],
    [-3, 7, 0],
    [-8, 1, 3]
]).T.rref()
pprint(R)
print('rank', len(p))

print('f')
R, p = Matrix([
    [-5, 2, 3],
    [7, 1, 0],
    [-7, 6, 1],
    [-2, 5, 2]
]).T.rref()
pprint(R)
print('rank', len(p))
