def f(a):
    c = ''
    while a > 0:
        c += str(a % 3)
        a = a // 3
    c = c[::-1]
    return c
for n in range(300):
    r = f(n)
    if n % 3 == 0:
        r = '1' + r + '02'
    else:
        r = r + f((n % 3) * 4)
    r = int(r, 3)
    if r < 199:
        print(n)
