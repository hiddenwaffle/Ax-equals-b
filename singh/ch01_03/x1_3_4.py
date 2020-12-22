import numpy as np
from util.graph import Graph

u = np.array([2, -1])

g = Graph()
g.append(u)
g.append(-u)
g.append(2 * u)
g.append(3 * u)
g.append(-2 * u)
g.show()
