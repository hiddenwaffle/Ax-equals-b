from sympy import *
from util.graph import Graph

g = Graph()

x = Matrix([1, 2])
g.add_vector(x)

A = Matrix([
    [2, 0],
    [0, 2]
])
b = A * x
g.add_vector(b, color='tab:blue')

A = Matrix([
    [-1, 0],
    [0, -1]
])
b = A * x
g.add_vector(b, color='tab:green')

g.show()

