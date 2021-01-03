from sympy import *


# Definiting the inner product to be:
# <X, Y> = tr(Y.T @ X)
def ip(a, b):
    return (b.T @ a).trace()


def main():
    A = Matrix([
        [-1, -1],
        [1, 5]
    ])
    B = Matrix([
        [1, 2],
        [3, 0]
    ])
    print(ip(A, B))


if __name__ == '__main__':
    main()
