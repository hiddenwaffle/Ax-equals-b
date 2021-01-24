from sympy import *
from util.graph import Graph


def orthogonal(u, v):
    return v - ((u.T * v) / u.norm() ** 2)[0] * u


g = Graph()

v1 = Matrix([1, 1])
v2 = Matrix([2, 1])
w1 = v1.copy()
w2 = orthogonal(w1, v2)
w1 = w1 / w1.norm()
w2 = w2 / w2.norm()
g.add_vector(w1)
g.add_vector(w2)
pprint([w1, w2])
# ⎡⎡√2⎤  ⎡ √2 ⎤⎤
# ⎢⎢──⎥  ⎢ ── ⎥⎥
# ⎢⎢2 ⎥  ⎢ 2  ⎥⎥
# ⎢⎢  ⎥, ⎢    ⎥⎥
# ⎢⎢√2⎥  ⎢-√2 ⎥⎥
# ⎢⎢──⎥  ⎢────⎥⎥
# ⎣⎣2 ⎦  ⎣ 2  ⎦⎦

v1 = Matrix([2, 1])
v2 = Matrix([1, 1])
w1 = v1.copy()
w2 = orthogonal(w1, v2)
w1 = w1 / w1.norm()
w2 = w2 / w2.norm()
g.add_vector(w1, color='tab:blue')
g.add_vector(w2, color='tab:blue')
pprint([w1, w2])
# ⎡⎡2⋅√5⎤  ⎡-√5 ⎤⎤
# ⎢⎢────⎥  ⎢────⎥⎥
# ⎢⎢ 5  ⎥  ⎢ 5  ⎥⎥
# ⎢⎢    ⎥, ⎢    ⎥⎥
# ⎢⎢ √5 ⎥  ⎢2⋅√5⎥⎥
# ⎢⎢ ── ⎥  ⎢────⎥⎥
# ⎣⎣ 5  ⎦  ⎣ 5  ⎦⎦

g.show()
# They are mirror images of each other
