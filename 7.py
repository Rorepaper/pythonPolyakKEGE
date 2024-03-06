def f(a):
    c = ''
    while a > 0:
        c += str(a % 64)
        a = a // 64
    c = c[::-1]
    return c
s = 7 * 512 ** 3200 + 6 * 256 ** 3100 - 5 * 64 ** 3000 - 4 * 8 ** 2900 - 1542
k = f(s)
print(k.count('0'))