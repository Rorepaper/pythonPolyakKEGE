from fnmatch import fnmatch
for n in range(2023, 10 ** 9 + 1, 2023):
    s = str(n)
    su = sum(map(int, s))
    if su % 7 == 0 and su < 20 and fnmatch(s, "20*23"):
        print(n)