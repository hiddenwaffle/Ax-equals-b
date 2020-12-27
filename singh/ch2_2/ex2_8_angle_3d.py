import numpy as np
from math import acos, degrees

u = np.array([3, -1, 7])
v = np.array([-2, 1, 9])

n = u @ v
d = np.linalg.norm(u) * np.linalg.norm(v)
angle_cos = n / d
angle = degrees(acos(angle_cos))
print(angle)
