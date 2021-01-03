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
    # TODO


if __name__ == '__main__':
    main()
