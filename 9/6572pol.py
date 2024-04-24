c = 0
for i in __import__("csv").reader(open("6572pol.csv")):
    i = list(map(int, i))
    if all(j != max(i) and j != min(i) for j in [i[0], i[-1]]):
        sp = i[:]
        [sp.remove(j) for j in [max(i), min(i)]]
        try:
            if (max(i) - min(i)) % (max(sp) - min(sp)) == 0:
                c += 1
        except ZeroDivisionError:
            continue
print(c)
