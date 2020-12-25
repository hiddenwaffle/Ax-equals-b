import numpy as np
from numpy.linalg import matrix_power
from fractions import Fraction

A = np.array([
    [Fraction(1, 3), Fraction(1, 3), Fraction(1, 3)],
    [Fraction(1, 3), Fraction(1, 3), Fraction(1, 3)],
    [Fraction(1, 3), Fraction(1, 3), Fraction(1, 3)]
])

print(A)
print(matrix_power(A, 2))
print(matrix_power(A, 3))
# looks like it is always the same
# i tried with 1/4 but it did not do the same thing; something special about 1/3,
# maybe because it has it is a 3x3 matrix?
# i tried it with 1/4 on a 4x4 matrix and it did the same thing
