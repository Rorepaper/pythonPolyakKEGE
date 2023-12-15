def pr(n):
    c = True
    for j in range(2, n):
        if n % j == 0:
            c = False
    return c


for n in range(101, 10000):
    s = "0" + "2" * 50 + "1" * n + "0"

    while "00" not in s:
        for i in [["02", "101"], ["11", "2"], ["012", "30"], ["010", "00"]]:
            s = s.replace(i[0], i[1], 1)
    if pr(sum(list(map(int, list(s))))):
        print(n)
        break
