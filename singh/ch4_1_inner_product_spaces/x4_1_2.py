from sympy import *


def ip(f, g):
    x = symbols('x')
    return integrate(f * g, (x, -1, 1))


def norm(f):
    return sqrt(ip(f, f))


def main():
    x = symbols('x')
    f = x
    g = x ** 3
    print('a', ip(f, g))
    print('b', ip(g, f))
    print('c', ip(3 * f, g))
    print('d', ip(f, f))
    print('e', norm(f))
    print('f', ip(g, g))
    print('g', norm(g))


if __name__ == '__main__':
    main()
