import sys

sys.setrecursionlimit(9 ** 9)


def f(n):
    if n < 9:
        return n // 3 + n % 3
    else:
        return f(n // 9) + f(n % 9)

c = 0
for n in range(1, 9 ** 9):
    if f(n) == 33:
        c += 1