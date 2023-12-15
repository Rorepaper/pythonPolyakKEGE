for n in range(1000012, 10**9, 13):
    s = str(n)
    if s[:2] == "24" and s[-5:-3] == "68" and s[-3] in "39" and s[-2:] == "35":
        s1 = s[2:-5]
        fl = 1
        for sym in s1:
            if int(sym) % 2 != 0:
                fl = 0
                break
        if fl:
            print(n, n // 13)