from sympy import *


# Definiting the inner product to be:
# <X, Y> = tr(Y.T @ X)
def ip(a, b):
    return (b.T @ a).trace()


def norm(a):
    return sqrt(ip(a, a))


def main():
    A = Matrix([
        [3, 7],
        [5, 4]
    ])
    B = Matrix([
        [2, 1],
        [7, -12]
    ])
    print('a')
    print(ip(A, B))
    print('b')
    print(norm(A + B))


if __name__ == '__main__':
    main()
