from sympy import *

print('a')
M = Matrix([
    [1, -1, -2, -3],
    [-4, 4, 8, 12]
])
R, p = M.rref()
pprint(R)
print(p)
Ab = Matrix([
    [1, -1, -2, -3, 5],
    [-4, 4, 8, 12, 2]
])
R, p = Ab.rref()
pprint(R)
print(p)
print('no solution, ranks are different')

print('b')
M = Matrix([
    [1, 2, 3, 1],
    [4, 5, 6, 2],
    [7, 8, 8, 3]
])
R, p = M.rref()
pprint(R)
print(p)
print('unique solution, both have the same rank, and is full')
