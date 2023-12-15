from fnmatch import fnmatch


def pr(n):
    c = []
    for d in range(1, int(n ** 0.5) + 1):
        if n % d == 0:
            c.append(d)
            c.append(n // d)
    return c


for n in range(53, 10 ** 7, 53):
    dels = pr(n)
    if fnmatch(str(n), "*2?2*") and str(n) == str(n)[::-1] and len(dels) > 30:
        print(n, sum(dels))
