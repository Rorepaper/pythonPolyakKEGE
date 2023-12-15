from fnmatch import fnmatch
for n in range(211, 10 ** 8 + 1, 211):
    if fnmatch(str(n), "11??4*56"):
        print(n, n // 211)