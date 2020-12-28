# https://docs.sympy.org/latest/tutorial/printing.html
import numpy as np
from sympy import *
from sympy.printing.dot import dotprint
from sys import exit

init_printing(use_unicode=True)

x, y, z = symbols('x y z')
print(str(Integral(sqrt(1 / x), x)))
print(srepr(Integral(sqrt(1 / x), x)))
pprint(Integral(sqrt(1 / x), x), use_unicode=False)
s = pretty(Integral(sqrt(1 / x), x), use_unicode=False)
print(s)
pprint(Integral(sqrt(1 / x), x), use_unicode=True)
print(latex(Integral(sqrt(1 / x), x)))
print(dotprint(x + 2))

exit()
