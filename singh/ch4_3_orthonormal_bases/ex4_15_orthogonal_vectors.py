from sympy import *
from util.graph import Graph


def orthogonal(u, v):
    return v - ((u.T * v) / u.norm() ** 2)[0] * u


def main():
    g = Graph()

    v1 = Matrix([[3, 0]]).T
    v2 = Matrix([[1, 2]]).T
    g.add_vector(v1, color='tab:green')
    g.add_vector(v2, color='tab:red')

    p1 = v1.copy()
    p2 = orthogonal(p1, v2)
    pprint([p1, p2])
    g.add_vector(p1, color='tab:blue')  # same as v1 (green) so it hides it
    g.add_vector(p2, color='tab:orange')

    g.show()


if __name__ == '__main__':
    main()
