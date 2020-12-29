import numpy as np
from math import acos, degrees
from util.graph import Graph

u = np.array([-5, -1])
v = np.array([4, 2])

n = u @ v
d = np.linalg.norm(u) * np.linalg.norm(v)
cos_angle = n / d
angle = acos(cos_angle)
print(f'{degrees(angle)} degrees')

g = Graph()
g.add_vector(u, color='b')
g.add_vector(v, color='g')
g.show()
