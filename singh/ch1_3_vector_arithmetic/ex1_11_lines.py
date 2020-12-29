import numpy as np
from util.graph import Graph

v = np.array([3, 1])

g = Graph()
g.add_vector(0.5 * v)
g.add_vector(2 * v)
g.add_vector(3 * v)
g.add_vector(-v)
g.show()
