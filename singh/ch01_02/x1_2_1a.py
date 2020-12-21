from fractions import Fraction
import numpy as np

m = np.array([
    [1, 1, 7],
    [1, -2, 4]
])
m = m.astype(float)
print(m, "\n", '---')

# Subtract the first row from the second (already has a 1)
m[1] -= m[0]
print(m, "\n", '---')

# Flatten second row to a 1
# Cannot use *= here because of typing issues?
m[1] = m[1] * Fraction(-1, 3)
print(m, "\n", '---')

# Subtract row 2 from row 1 (already has a 1)
m[0] -= m[1]
print(m, "\n", '---')

print(m[:, 2])
