import numpy as np

m1 = np.array([
    [5, -1, -2],
    [10, -2, -4],
    [15, -3, -6]
])
m2 = np.array([
    [1, 1, 3],
    [1, -1, -1],
    [2, 3, 8]
])
print(m1 @ m2)

# multiplying m1 and m2 created a zero matrix
# unlike regular multiplication, it possible to get a zero result without zero in either operand
