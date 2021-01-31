from sympy import *

T = diff
x = symbols('x')
B = Matrix([1, x, x ** 2])
C = Matrix([1, x])
p = 2 * x ** 2 + 3 * x + 1
print('Apply T to each polynomial in B')
pprint(T(1))
pprint(T(x))
pprint(T(x ** 2))
print('Matrix A is each polynomial in B as coordinates of C')
A = Matrix([
    [0, 1, 0],
    [0, 0, 2]
])
pprint(A)
pB = Matrix([[1, 3, 2]]).T
print('The coefficients of the polynomial p in C')
pprint(A * pB)
print('These match the derivative of p')
pprint(diff(p))

print('Can be used on another polynomial in B to find it in C')
qB = Matrix([[7, 5, 3]]).T
pprint(A * qB)
