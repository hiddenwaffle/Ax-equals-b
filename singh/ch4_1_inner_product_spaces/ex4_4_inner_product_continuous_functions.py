from sympy import *


def ip(f, g):
    x = symbols('x')
    return integrate(f * g, (x, 0, 1))


def main():
    print('(i) <f,g>')
    x = symbols('x')
    f = x
    g = x ** 2 - 1
    pprint(ip(f, g))
    print('(ii) ||f||')
    pprint(sqrt(ip(f, f)))
    print('(iii) ||g||')
    pprint(sqrt(ip(g, g)))
    print('(iv) ||f - g||')
    # Errata p285
    # I think the book is mistakenly subtracting g = x ** 2 + 1 instead
    pprint(sqrt(ip(f - g, f - g)))
    h = x ** 3
    print('(v) ||f - h|| where h = x ** 3')
    pprint(sqrt(ip(f - h, f - h)))


if __name__ == '__main__':
    main()
