from sympy import *

A = Matrix([
    [2, 0],
    [1, 3]
])
# find lambdas that satisfy the characteristic equation
λ = symbols('λ')
AminyI = A - λ * eye(2)
print('AminyI')
pprint(AminyI)
det = AminyI.det()
print('det', det)
eigenvalues = solve(det, λ)
print('eigenvalues:', eigenvalues)
# use the eigenvalues to find the eigenvectors
x, y = symbols('x, y')
# first try 2
Amin2I = A - 2 * eye(2)
u = Matrix([[x, y]]).T
eq = Eq(MatMul(Amin2I, u), zeros(2, 1), evaluate=False)
pprint(eq)
print('eigenvectors:', solve(eq, x, y))
# next try 3
Amin3I = A - 3 * eye(2)
u = Matrix([[x, y]]).T
eq = Eq(MatMul(Amin3I, u), zeros(2, 1), evaluate=False)
pprint(eq)
print('eigenvectors:', solve(eq, x, y))  # assuming y means "any real #"?
