import numpy as np

u = np.array([-1, 3, 2, 0])
v = np.array([3, -2, 5, 1])
w = np.array([0, -1, 1, 2])

print('a', u + v + w)
print('b', u - v - w)
print('c', u - 2 * v + 3 * w)

print('d (part 1)', u - 3 * w)

# part 2:
# x - 1
# y + 6
# z - 1
# a - 6

# part 3:
print(-(u + v + w))  # negated because of moving the x onto the right side
