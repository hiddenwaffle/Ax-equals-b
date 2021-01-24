from sympy import *


def ip(p: Poly, q: poly):
    return sum(map(prod, zip(p.coeffs(), q.coeffs())))


def norm(p: Poly):
    return sqrt(ip(p, p))


def main():
    x = symbols('x')
    p = Poly(5 * x ** 2 - 2 * x + 1)
    print(norm(p))


if __name__ == '__main__':
    main()
