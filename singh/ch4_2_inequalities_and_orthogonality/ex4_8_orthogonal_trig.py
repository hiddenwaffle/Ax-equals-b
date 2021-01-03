from sympy import *


def ip(f, g):
    t = symbols('t')
    return integrate(f * g, (t, 0, pi))


def main():
    t = symbols('t')
    f = cos(t)
    g = sin(t)
    print(ip(f, g))


if __name__ == '__main__':
    main()
