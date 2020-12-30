from sympy import *

print('a')
A = Matrix([
    [1, -4, -9],
    [2, 5, -7]
])
R, _ = A.rref()
row_space = [
    R.row(0).T * 13,
    R.row(1).T * 13
]
print('row space:')
pprint(row_space)
R, _ = A.T.rref()
column_space = [
    R.row(0).T,
    R.row(1).T
]
print('column space:')
pprint(column_space)

s = symbols('s')
x = Rational(73, 13) * s
y = Rational(-11, 13) * s
z = s
u = Matrix([x, y, z])
u = MatMul(s, u * 13 / s)  # can * by 13 because 13 is just a constant scalar
pprint(u)
pprint('rank 2 nullity 1')

