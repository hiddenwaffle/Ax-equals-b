import numpy as np
from math import acos, degrees, sqrt


def angle(u, v):
    n = u @ v
    d = np.linalg.norm(u) * np.linalg.norm(v)
    return degrees(acos(n / d))


def main():
    u = np.array([-1, 1, 3])
    v = np.array([3, -1, 5])
    print('a', angle(u, v))
    u = np.array([1, 0, 0,])
    v = np.array([0, 0, 15])
    print('b', angle(u, v))
    u = np.array([-1, 2, 3])
    v = np.array([sqrt(2), 1/sqrt(2), -1])
    print('c', angle(u, v))


if __name__ == '__main__':
    main()
