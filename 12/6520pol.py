def f(n):
    sp = []
    for d in range(2, int(n ** 0.5)+1):
        if n % d == 0:
            sp.append(d)
            sp.append(n // d)
    return set(sp)


for n in range(4, 100):
    s = "3" + "7" * n
    while any(i in s for i in ["37", "577", "777"]):
        for i in [["37", "7"], ["577", "73"], ["777", "5"]]:
            if i[0] in s:
                s = s.replace(i[0], i[1], 1)

    s = sum(map(int, s))

    if len(str(s)) == 2:
        if not f(int(s)).intersection(f(n)):
            print(n)