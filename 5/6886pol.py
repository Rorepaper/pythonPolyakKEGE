def trin(n):
    sp = []
    while n:
        sp.append(n % 3)
        n //= 3
    return sp[::-1]


for n in range(10000):
    n3 = trin(n)
    s = sum(n3)
    n3 = "".join(list(map(str, n3)))
    if s % 3 == 0:
        n3 = "20" + n3
    else:
        n3 = "10" + n3
    r = int(n3, 3)
    if r < 100:
        print(n)