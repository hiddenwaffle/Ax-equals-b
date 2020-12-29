from sympy import *

AO = Matrix([
    [1, 2, 3, 0],
    [4, 5, 6, 0],
    [7, 8, 9, 0]
])
R, p = AO.rref()
pprint(R)
pprint(p)

# x = z
# y = -2z
# z is free
# Answer:-------
x, y, z, s = symbols('x y z s')
vx = Matrix([x, y, z])
pprint(vx)
vx = vx.subs({x: s, y: -2 * s, z: s})
pprint(vx)
# factor out the s: https://stackoverflow.com/a/39692039
vx_gcd = gcd(tuple(vx))  # determine factor (step 1)
u = vx / vx_gcd  # factor out the factor (step 2)
eq = MatMul(vx_gcd, u, evaluate=False)  # put the factor in front (step 3)
pprint(eq)
print(pretty(u.T), 'is a basis vector on the axis of the solution space')
