import numpy as np
from math import acos, degrees


def angle(u, v):
    n = u @ v
    d = np.linalg.norm(u) * np.linalg.norm(v)
    return degrees(acos(n / d))


def main():
    u = np.array([-1, 1, 3])
    v = np.array([3, -1, 5])
    print('a', angle(u, v))
    # TODO


if __name__ == '__main__':
    main()
