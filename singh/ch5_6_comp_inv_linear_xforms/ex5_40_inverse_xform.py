from sympy import *

print('i')
B = Matrix([
    [1, -1],
    [1, 1]
])
pprint(B)
A = B.inv()
pprint(A)
print('ii')
pprint(B * A)
