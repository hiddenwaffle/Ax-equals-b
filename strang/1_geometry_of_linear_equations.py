# row "picture" shows the x in Ax=b
# column "picture" shows the b in Ax=b

import numpy as np
from sympy import *
from util.graph import Graph

print('a system of 2 equations')
x, y = symbols('x y')
eq1 = Eq(2 * x - y, 0)
eq2 = Eq(-x + 2 * y, 3)
pprint(eq1)
pprint(eq2)
result = linsolve([eq1, eq2], [x, y])
print('x, y:', pretty(result))

# row "picture"
# See an intersection at [1, 2]
g_row = plot(solve(eq1, y)[0], show=False, line_color='tab:blue', xlim=[-5, 5], ylim=[-5, 5])
g_row.append(plot(solve(eq2, y)[0], show=False, line_color='tab:blue')[0])
g_row.show()

# col "picture"
g_col = Graph()
M, b = linear_eq_to_matrix([eq1, eq2], x, y)
# Show the columns vectors in green
u = np.array(M.col(0)).T[0]
v = np.array(M.col(1)).T[0]
g_col.add_vector(u, color='tab:green')
g_col.add_vector(v, color='tab:green')
# Show [0, 3] in orange (2x the second column, added to the first)
w = 2 * v
g_col.add_vector(w, start=u, color='tab:orange')
g_col.show()
