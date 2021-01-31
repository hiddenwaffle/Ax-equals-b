from sympy import *

A = Matrix([
    [2, 1, 3],
    [0, 2, 0],
    [0, 0, 2]
])
pprint(A.eigenvects())
# 2 has multiplicity 3)

# Calculate manually:
lmbda = symbols('lmbda')
AminlmbdaI = A - MatMul(lmbda, eye(3), evaluate=False)
pprint(AminlmbdaI)
eq = Eq(AminlmbdaI.det(), 0)
pprint(eq)
pprint(solve(eq, lmbda))
# lmbda == 2
x, y, z = symbols('x y z')
u = Matrix([[x, y, z]]).T
Amin2I = A - 2 * eye(3)
eq = Eq(MatMul(Amin2I, u), zeros(3, 1), evaluate=False)
pprint(eq)
pprint(solve(eq, x, y, z))  # and x and z are any real #
