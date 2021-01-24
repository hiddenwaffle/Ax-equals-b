from sympy import *
from util.graph import Graph

g = Graph()

print('a')
u = Matrix([[1, 1]]).T
v = Matrix([[-1, 1]]).T
pprint(u.T * v)
g.add_vector(u)
g.add_vector(v)

print('b')
u = Matrix([[-2, -3]]).T
v = Matrix([[3, -2]]).T
pprint(u.T * v)
g.add_vector(u, color='tab:blue')
g.add_vector(v, color='tab:blue')

print('c')
u = Matrix([[-4, 5]]).T
v = Matrix([[5, 4]]).T
pprint(u.T * v)
g.add_vector(u, color='tab:green')
g.add_vector(v, color='tab:green')

print('d')
u = Matrix([[2, 7]]).T
v = Matrix([[-7, 2]]).T
pprint(u.T * v)
g.add_vector(u, color='tab:orange')
g.add_vector(v, color='tab:orange')

g.show()

