from sympy import *
from util.graph import Graph


def orthogonal(u, v):
    return v - ((u.T * v) / u.norm() ** 2)[0] * u


def normalize(v):
    norm = v.norm()
    if norm == 0:
        return v
    else:
        return v / norm


def main():
    g = Graph()

    v1 = Matrix([[2, 1]]).T
    v2 = Matrix([[1, 1]]).T
    g.add_vector(v1)
    g.add_vector(v2)

    p1 = v1.copy()
    p2 = orthogonal(p1, v2)
    g.add_vector(p1, color='tab:blue')
    g.add_vector(p2, color='tab:blue')

    n1 = normalize(p1)
    n2 = normalize(p2)
    g.add_vector(n1, color='tab:green')
    g.add_vector(n2, color='tab:green')

    g.show()


if __name__ == '__main__':
    main()
