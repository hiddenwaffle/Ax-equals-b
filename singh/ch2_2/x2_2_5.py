import numpy as np
from math import sqrt, pi


def normalize(v):
    norm = np.linalg.norm(v)
    return v / norm


print('a', normalize(np.array([2, 3])))
print('b', normalize(np.array([1, 2, 3])))
print('c', normalize(np.array([1/2, -1/2, 1/4])))
print('d', normalize(np.array([sqrt(2), 2, -sqrt(2), sqrt(2)])))
print('e', normalize(np.array([-pi/5, pi, -pi, pi/10, 0])))
