c = 0
for i in __import__("csv").reader(open("6455pol.csv")):
    i = list(map(int, i))
    d = {}
    for j in i:
        if j not in d:
            d[j] = 1
        else:
            d[j] += 1
    if d[min(i)] == 1:
        if len(set(i)) != 6:
            pov = []
            for j in i:
                if d[j] > 1:
                    pov.append(j)
            if max(i) + min(i) < sum(pov):
                c += 1
print(c)
