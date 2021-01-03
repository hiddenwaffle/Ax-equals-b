from sympy import *
from math import prod


def ip(p: Poly, q: poly):
    return sum(map(prod, zip(p.coeffs(), q.coeffs())))


def norm(p: Poly):
    return sqrt(ip(p, p))


def main():
    x = symbols('x')
    p = Poly(2 - 3 * x + 5 * x ** 2)
    q = Poly(7 + 5 * x - 4 * x ** 2)
    print('a', ip(p, q))
    print('b', ip(q, p))
    print('c', ip(p, -3 * q))
    print('d', ip(p, p))
    print('e', norm(p))
    print('f', ip(q, q))
    print('g', norm(q))


if __name__ == '__main__':
    main()
