from sympy import *
from util.graph import Graph

g = Graph()

P = Matrix([[0, 0]]).T
Q = Matrix([[2, 0]]).T
R = Matrix([[0, 3]]).T
g.add_vector(P, color='tab:blue')
g.add_vector(Q, color='tab:blue')
g.add_vector(R, color='tab:blue')

A = Matrix([
    [P, Q, R]
])
B = Matrix([
    [2, 0],
    [3, 4]
])
BA = B * A

g.add_vector(BA.col(0), color='tab:green')
g.add_vector(BA.col(1), color='tab:green')
g.add_vector(BA.col(2), color='tab:green')

print('determinant of B:', B.det())

g.show()
