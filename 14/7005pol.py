def pr(n):
    for d in range(2, n):
        if n % d == 0:
            return False
    return True


for y in range(18):
    for x in range(11):
        a = 4 + x * 12 + 9 * 12 ** 2 + x * 12 ** 3 + 5 * 12 ** 4
        b = 6 + x * 14 + x * 14 ** 2 + 7 * 14 ** 3
        c = 8 + x * 16 + x * 16 ** 2 + 5 * 16 ** 3 + 5 * 16 ** 4
        d = 7 + x * 19 + y * 19 ** 2 + 3 * 19 ** 3
        r = a + b + c - d
        if pr(r):
            print(x * y)