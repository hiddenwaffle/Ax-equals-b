from sympy import *
from util.graph import Graph

Q = (1 / sqrt(2)) * Matrix([
    [1, 1],
    [1, -1]
])
u = Matrix([[1, 2]]).T

print('i')
pprint(u.norm())
print('ii')
pprint((Q * u).norm())

g = Graph()
g.add_vector(u, color='tab:blue')
g.add_vector(Q * u, color='tab:green')
g.show()

# Q changed u's direction but not its length
