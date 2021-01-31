from sympy import *

A = Matrix([
    [3, 2],
    [3, 4]
])
lmbda = symbols('lmbda')
AminlambdaI = A - lmbda * eye(2)
pprint(AminlambdaI)
charpoly = AminlambdaI.det()
print('charpoly', charpoly)
# substitute A into this question
part1 = charpoly.subs(lmbda, A)  # part1 because 6 needs to be 6I (?)
part2 = part1 - 6 + 6 * eye(2)
pprint(part2)
# thus, p(A) = the zero vector
