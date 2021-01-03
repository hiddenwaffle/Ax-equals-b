from sympy import *


# Definiting the inner product to be:
# <X, Y> = tr(Y.T @ X)
def ip(a, b):
    return (b.T @ a).trace()


def norm(a):
    return sqrt(ip(a, a))


def main():
    A = Matrix([
        [1, 2],
        [3, 4]
    ])
    B = Matrix([
        [5, 6],
        [7, 8]
    ])
    C = Matrix([
        [-1, 1],
        [2, 5]
    ])
    print('a', ip(A, B))
    print('b', ip(5 * A, B))
    print('c', ip(-A, -B))
    print('d', norm(A))
    print('e', norm(B))
    print('f', ip(A, C))
    print('g', ip(B, C))
    print('h', ip(A + B, C))
    print('i', ip(A, C + B))


if __name__ == '__main__':
    main()
