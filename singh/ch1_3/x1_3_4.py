import numpy as np
from util.graph import Graph

u = np.array([2, -1])

g = Graph()
g.add_vector(u)
g.add_vector(-u)
g.add_vector(2 * u)
g.add_vector(3 * u)
g.add_vector(-2 * u)
g.show()
