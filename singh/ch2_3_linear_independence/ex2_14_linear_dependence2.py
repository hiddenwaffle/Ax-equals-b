import numpy as np
from sympy import *

u = np.array([2, 3, 7])
v = np.array([-4, 19, -5])
w = np.zeros(3)

A = Matrix([
    u, v, w, np.zeros(3)
]).T
A, _ = A.rref()
pprint(A)
# The presence of a zero vector ensures that the vectors are linearly dependent
