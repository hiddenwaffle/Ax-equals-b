from sympy import *

print('a')
M = Matrix([
    [2, 8],
    [7, 28]
])
pprint(M.rref())
Ma = Matrix([
    [2, 8, 12],
    [7, 28, 42]
])
pprint(Ma.rref())
print('both rank 1 < 2 unknowns = infinite solutions')

print('b')
M = Matrix([
    [2, -3, -6, 12],
    [3, -5, -7, 16]
])
R, _ = M.rref()
pprint(R)
Ma = Matrix([
    [2, -3, -6, 12, 2],
    [3, -5, -7, 16, 5]
])
R, _ = Ma.rref()
pprint(R)
print('infinite solutions')

print('c')
M = Matrix([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
Ma = M.row_join(Matrix([1, 2, 4]))
pprint(Ma)
pprint(M.rref())
pprint(Ma.rref())
print('no solution')

print('d')
M = Matrix([
    [2, 5, -3, -7],
    [1, 1, -4, -8],
    [3, 4, 0, 1],
    [5, 21, -1, 3]
])
Ma = M.row_join(Matrix([0, 9, 6, 2]))
pprint(M.rref())
pprint(Ma.rref())
print('unique solution')
pprint(Ma.rref()[0].col(4))
