import numpy as np
from math import acos, degrees


def angle(u, v):
    n = u @ v
    d = np.linalg.norm(u) * np.linalg.norm(v)
    return degrees(acos(n / d))


def main():
    u = np.array([1, 1])
    v = np.array([0, 1])
    print('a', angle(u, v))
    u = np.array([1, 0])
    v = np.array([0, 1])
    print('b', angle(u, v))
    u = np.array([-2, 3])
    v = np.array([1/2, -1/2])
    print('c', angle(u, v))


if __name__ == '__main__':
    main()
