from sympy import *

A = Matrix([
    [2, 7],
    [3, 8],
    [4, 9]
])
B = Matrix([
    [1, 6],
    [0, 0]
])
AB = A * B
pprint(AB)
# number of columns in A must match the number of rows in B
# 4 ways to think of this:
#   1) "ABij = (row i of A) * (column j of B)"
#   2) "columns of AB are combinations of columns of A"
#   3) "rows of AB are combinations of rows of B"
#   4) "AB = sum of (columns of A) * (rows of B)

# illustration of #4
way4 = MatAdd(
    MatMul(A.col(0), B.row(0)),
    MatMul(A.col(1), B.row(1)),
    evaluate=False
)
pprint(way4)
print('way 4 == AB:', Eq(way4.doit(), AB))

# "Blocks"
# https://youtu.be/FX4C-JpTFgY?t=1131
a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p = symbols('a b c d e f g h i j k l m n o p')
A1 = Matrix([
    [a, b],
    [c, d]
])
A2 = Matrix([
    [e, f],
    [g, h]
])
A3 = Matrix([
    [i, j],
    [k, l]
])
A4 = Matrix([
    [m, n],
    [o, p]
])
A = BlockMatrix([
    [A1, A2],
    [A3, A4]
])
# Upper left of AA when multiplying only block matrices
pprint((A1 * A1 + A2 * A3).col(0)[0])
# Upper left of AA when multiplying the whole matrix
pprint(Matrix((A * A)).col(0)[0])
# They are the same
