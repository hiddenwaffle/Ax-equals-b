import numpy as np
from util.graph import Graph
from math import acos, cos, sin, pi, degrees

print('b')
u = np.array([cos(pi/4), sin(pi/4)])
print(u)

print('c')
v = np.array([cos(pi/4), -sin(pi/4)])

print('d')
n = u @ v
d = np.linalg.norm(u) * np.linalg.norm(v)
angle_cos = n / d
angle = acos(angle_cos)
print(degrees(angle))

g = Graph()
g.add_vector(u, color='g')
g.add_vector(v, color='b')
g.show()
