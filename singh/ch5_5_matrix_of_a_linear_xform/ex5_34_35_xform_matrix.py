from sympy import *

print('ex34')
v1 = Matrix([[1, 1, 1]]).T
v2 = Matrix([[-1, 0, 1]]).T
v3 = Matrix([[0, 0, 1]]).T
B = Matrix([
    [v1, v2, v3]
])
w1 = Matrix([[1, 2]]).T
w2 = Matrix([[-1, 1]]).T
C = Matrix([
    [w1, w2]
])
# Write T as a matrix (this is my own step)
T = Matrix([
    [3, 1, 1],
    [1, -3, -1]
])
# Apply T to the vectors in B
Tv1 = T * v1
Tv2 = T * v2
Tv3 = T * v3
# Write these vectors as the coordinates of C
# v1
a, b = symbols('a b')
eq = Eq(Tv1, a * w1 + b * w2)
ab = solve(eq, a, b)
a = ab[a]
b = ab[b]
# v2
c, d = symbols('c d')
eq = Eq(Tv2, c * w1 + d * w2)
cd = solve(eq, c, d)
c = cd[c]
d = cd[d]
# v3
e, f = symbols('e f')
eq = Eq(Tv3, e * w1 + f * w2)
ef = solve(eq, e, f)
e = ef[e]
f = ef[f]
# Assemble A from these solutions (is there a better way to do this?)
A = Matrix([
    [a, c, e],
    [b, d, f]
])
pprint(A)

print('ex35')
u = Matrix([[1, 0, 2]]).T
a, b, c = symbols('a b c')
eq = Eq(u, a * v1 + b * v2 + c * v3)
abc = solve(eq, a, b, c)
a = abc[a]
b = abc[b]
c = abc[c]
# Construct the vector uB from these solutions
uB = Matrix([[a, b, c]]).T
# Finally, the transformation of u with respect to the basis C
pprint(A * uB)
