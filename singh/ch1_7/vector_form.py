import numpy as np

# x1 = 2 + s + t
# x2 = 7 - s
# x3 = 6 - t
# x4 = 6 - s - t
# x5 = s
# x6 = t

m = np.array([
    [1, 1, 2],      # x1
    [-1, 0, 7],     # x2
    [0, -1, 6],     # x3
    [-1, -1, 6],    # x4
    [1, 0, 0],      # x5
    [0, 1, 0]       # x6
])
print(m)
# and multiply this by:
# [s, t, 1].T
# (at least, I think 1 is how you would get the 3rd column to be a constant)
