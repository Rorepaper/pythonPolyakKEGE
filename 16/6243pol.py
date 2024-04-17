__import__("sys").setrecursionlimit(1000000)


def f(n):
    if n <= 2:
        return n
    else:
        return n + f(n - 2)


print(f(2023) + f(2020))
