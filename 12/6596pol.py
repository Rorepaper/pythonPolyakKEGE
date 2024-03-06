for n in range(4, 1000):
    s = "2" + "5" * n
    while "25" in s or "35" in s or "555" in s:
        for i in [["25", "53"], ["35", "2"], ["555", "23"]]:
            if i[0] in s:
                s = s.replace(i[0], i[1], 1)
    if sum(map(int, list(s))) % 7 == 0:
        print(n)
        break