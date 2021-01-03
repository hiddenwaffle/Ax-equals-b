from sympy import *


def ip(f, g):
    x = symbols('x')
    return integrate(f * g, (x, 0, 1))


def norm(f):
    return sqrt(ip(f, f))


def main():
    x = symbols('x')
    f = x + 1
    g = x ** 2
    h = x - 1
    print('a', ip(f, g))
    print('b', ip(g, h))
    print('c', ip(f, h))
    print('d', ip(f + g, h))
    print('e', ip(f, h + g))
    print('f', ip(f + 3 * g, h))
    print('g', ip(f - 3 * g, h))
    print('h', ip(f - g, h))
    print('i', ip(2 * f + 5 * g, 6 * h))
    print('j', ip(-10 * f, 2 * h + 5 * g))


if __name__ == '__main__':
    main()
