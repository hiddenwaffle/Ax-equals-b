from sympy import *
from util.graph import Graph

T = Matrix([
    [1, -1],
    [1, 1]
])
S = Matrix([
    [2, 3],
    [1, -5]
])

g = Graph()

v = Matrix([[2, 3]]).T
g.add_vector(v)

result = S * T * v
pprint(result)
g.add_vector(result)

result = T * S * v
pprint(result)
g.add_vector(result)

# 38, shows they are the same
ST = S * T
pprint(ST * v)
TS = T * S
pprint(TS * v)

g.show()
