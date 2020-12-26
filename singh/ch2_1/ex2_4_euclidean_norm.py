import numpy as np
from util.graph import Graph

u = np.array([-7, -2])
v = np.array([8, 3])

print(f'‖u‖: {np.linalg.norm(u)}')
print(f'‖v‖: {np.linalg.norm(v)}')

g = Graph()
g.add_vector(u, color='tab:blue')
g.add_vector(v, color='tab:green')
g.show()
