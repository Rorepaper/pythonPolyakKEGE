def pr(n):
    for d in range(2, int(n ** 0.5) + 1):
        if not(n % d):
            return False
    return True


for n in range(51, 10000):
    s = "0" + "1" * 100 + "2" * n + "0"
    while "00" not in s:
        for i in [["02", "101"], ["11", "2"], ["012", "30"], ["010", "00"]]:
            s = s.replace(i[0], i[1], 1)

    if pr(sum(map(int, list(s)))):
        print(n)
        exit()