from sympy import *


# def ip(p: Poly, q: poly):
#     return sum(map(prod, zip(p.coeffs(), q.coeffs())))


def ip(q, r):
    x = symbols('x')
    return integrate(q * r, (x, -1, 1))


def norm(p):
    return sqrt(ip(p, p))


def orthogonal(u, v):
    return u - (ip(u, v) / norm(v) ** 2) * v


def orthogonal2(v3, p1, p2):
    ipv3p1 = ip(v3, p1)
    ipv3p2 = ip(v3, p2)
    np1sq = norm(p1) ** 2
    np2sq = norm(p2) ** 2
    return v3 - (ipv3p1 / np1sq) * p1 - (ipv3p2 / np2sq) * p2


def main():
    x = symbols('x')
    v1 = 1
    v2 = x
    v3 = x ** 2
    print('Manually:')
    p1 = v1
    p2 = orthogonal(v2, p1)  # notice that p2 = v2 (already orthogonal)
    p3 = orthogonal2(v3, p1, p2)
    pprint([p1, p2, p3])


if __name__ == '__main__':
    main()
