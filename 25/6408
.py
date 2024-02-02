from fnmatch import fnmatch
def pr(n):
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return True

for n in range(4019, 10**10, 4019):
    if fnmatch(str(n), "1?359*0") and pr(sum(map(int, str(n)))):
        print(n, n // 4019)
