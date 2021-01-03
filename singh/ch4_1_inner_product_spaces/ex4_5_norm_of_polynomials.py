from sympy import *


def norm(p):
    return sqrt(sum(map(lambda x: x * x, p.coeffs())))


def main():
    c0, c1, c2, x = symbols('c0 c1 c2 x')
    p = Poly(x ** 2 + x + 1)
    print('(i)', pretty(norm(p)))
    q = Poly(2 * x ** 2 + 2 * x + 2)
    print('(ii)', pretty(norm(q)))
    r = Poly(c2 * x ** 2 + c1 * x + c0, domain='ZZ[c0,c1,c2]')  # TODO: What is a domain?
    print('(iii)', pretty(norm(r)))


if __name__ == '__main__':
    main()
