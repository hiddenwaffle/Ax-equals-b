import numpy as np

s1 = np.array([1, 2, 3])
s2 = np.array([7, 4, 3])
s3 = np.array([2, 1, 9])

print(np.linalg.norm(s1 - s2))
print(np.linalg.norm(s1 - s3))
print(np.linalg.norm(s2 - s3))
