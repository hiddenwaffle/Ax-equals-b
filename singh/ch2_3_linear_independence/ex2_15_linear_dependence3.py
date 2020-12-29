import numpy as np
from sympy import *

u = np.array([-3, 1, 0])
v = np.array([0, 1, -1])
w = np.array([2, 0, 0])
x = np.array([1, 2, 3])
A, _ = Matrix([u, v, w, x, np.zeros(3)]).T.rref()
pprint(A)
# There are more variables than rows
# x is in terms of the other variables
