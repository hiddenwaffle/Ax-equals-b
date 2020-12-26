import numpy as np
from sympy import *

i = np.array([1, 0, 0])
j = np.array([0, 1, 0])
k = np.array([0, 0, 1])

print('a', i @ i)
print('b', j @ j)
print('c', k @ k)
print('d', i @ j)
print('e', i @ k)
print('f', j @ k)

a, b, c, d, e, f = symbols('a b c d e f')
u = a*i + b*j + c*k
v = d*i + e*j + f*k
pprint(u)
pprint(v)
pprint(u @ v)
