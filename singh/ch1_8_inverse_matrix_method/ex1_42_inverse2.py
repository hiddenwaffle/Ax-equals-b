from sympy import Matrix, pprint

print('a')
A = Matrix([
    [1, 0, 2, 1, 0, 0],
    [2, -1, 3, 0, 1, 0],
    [4, 1, 8, 0, 0, 1]
])
b = Matrix([
    [5],
    [7],
    [10]
])
Ai, p = A.rref()
# pprint(Ai)
# print(p)
Ai.col_del(0)
Ai.col_del(0)
Ai.col_del(0)
pprint((Ai * b).T)

print('b')
b = Matrix([
    [1],
    [2],
    [3]
])
pprint((Ai * b).T)
