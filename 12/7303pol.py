sp = []
for x in range(100):
    for y in range(150):
        s = "0" + "1" * y + "2" * x
        sb = s.count("1") + s.count("2") * 2
        if len(s) >= 95:
            while "01" in s or "02" in s:
                s = s.replace("02", "1110", 1)
                s = s.replace("01", "2210", 1)
            su = str(s.count("1") + s.count("2") * 2)
            if y == 92 and x == 2:
                print(su)
                exit()
            if su == su[::-1]:
                sp.append([sb, x, y])
print(sorted(sp))
