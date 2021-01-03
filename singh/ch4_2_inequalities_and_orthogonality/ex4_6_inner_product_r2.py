from sympy import *
from util.graph import Graph

u = Matrix([1, 2])
v = Matrix([3, 4])

i = u.T * v
print('(i)', pretty(i))

ii = u.norm() * v.norm()
print('(ii)', ii)

iii = u.norm() + v.norm()
print('(iii)', iii)

iv = (u + v).norm()
print('(iv)', iv)

g = Graph()
g.add_vector(u)
g.add_vector(v)
g.add_vector(u + v, color="tab:blue")
g.show()
