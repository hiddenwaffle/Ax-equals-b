from sympy import *


def letter_to_number(c):
    """Assumes that c is an uppercase letter in A-Z"""
    if c == ' ':
        return 30
    else:
        return ord(c) - 61


def number_to_letter(n):
    """Assumes that return value will be an uppercase letter in A-Z"""
    if n == 30:
        return ' '
    else:
        return chr(n + 61)


# https://stackoverflow.com/a/312464
def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


s = 'IS YOUR PARTNER HOME '
print('original:', s)
sn = list(map(letter_to_number, s))
snc = chunks(sn, 3)
msnc = Matrix(list(snc))
B = msnc.T
print('original matrix:')
pprint(B)

A = Matrix([
    [3, 4, 5],
    [1, 3, 1],
    [1, 1, 2]
])
Ai = A.inv()
AB = A * B
print('encoded matrix:')
pprint(AB)

print('decoded matrix:')
md = Ai * AB
pprint(md)

# https://stackoverflow.com/a/952952
flat = [x
        for y in md.T.tolist()
        for x in y]
s2 = ''.join(list(map(number_to_letter, flat)))
print('decoded:', s2)
