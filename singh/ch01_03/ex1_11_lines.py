import numpy as np
from util.graph import Graph

v = np.array([3, 1])

g = Graph()
g.append(0.5 * v)
g.append(2 * v)
g.append(3 * v)
g.append(-v)
g.show()
