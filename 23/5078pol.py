import sys
sys.setrecursionlimit(1000000)


def f1(a, b, oper):
    if a == b:
        return 1
    if a > b or a == 25 or a == 30:
        return 0

    if oper == 0:
        return f1(a+1, b, 0) + f1(a+2, b, 0) + f1(a * 3, b, 1)
    else:
        return f1(a + 1, b, 0) + f1(a + 2, b, 0)


print(f1(1, 15, 0)*f1(15, 43, 0))
