import numpy as np
from math import acos, degrees, sqrt, pi


def angle(u, v):
    n = u @ v
    d = np.linalg.norm(u) * np.linalg.norm(v)
    return degrees(acos(n / d))


def main():
    u = np.array([2, 3, -8, 1])
    v = np.array([-1, 2, -5, -3])
    print('a', angle(u, v))
    u = np.array([-2, -3, -1, -1])
    v = np.array([1, 2, 3, 4])
    print('b', angle(u, v))
    u = np.array([pi, sqrt(2), 0, 1])
    v = np.array([1 / pi, sqrt(2), -1, 1])
    print('c', angle(u, v))


if __name__ == '__main__':
    main()
