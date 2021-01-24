from sympy import *
from util.graph import Graph

u = Matrix([[-1, 1]]).T
v = Matrix([[-1, -1]]).T
pprint(u.T * v)
# orthogonal

b1 = u / u.norm()
b2 = v / v.norm()
pprint([b1, b2])

g = Graph()
g.add_vector(b1, color='tab:blue')
g.add_vector(b2, color='tab:green')
g.show()
