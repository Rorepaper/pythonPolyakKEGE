def pr(n):
    sp = []
    for d in range(1, int(n ** 0.5) + 1):
        if n % d == 0:
            if str(d)[0] == "4":
                sp.append(d)
            if str(n // d)[0] == "4":
                sp.append(n // d)
    return set(sp)


for i in range(10**6, 0, -1):
    if len(pr(i)) == 24:
        print(i, max(pr(i)))