from sympy import *


def ip(p: Poly, q: poly):
    return sum(map(prod, zip(p.coeffs(), q.coeffs())))


def norm(p: Poly):
    return sqrt(ip(p, p))


def main():
    x = symbols('x')
    p = Poly(x ** 2 + x + 1)
    q = Poly(-x ** 2 - x + 2)
    print(ip(p, q))


if __name__ == '__main__':
    main()
