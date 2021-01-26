from sympy import *

A = Matrix([
    [1, 2, 3],
    [4, 5, 6]
])

print('i')
Ao = A
A = A.row_join(zeros(2, 1))
pprint(A)
R = A.rref()
pprint(R)
pprint(linsolve(A))
# Therefore, u = [1, -2, 1] and ker(T) is any scalar multiple of this

# Checking with SymPy's built in method:
pprint(Ao.nullspace())
print('nullity', len(Ao.nullspace()))
