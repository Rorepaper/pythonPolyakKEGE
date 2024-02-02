from csv import reader
c = 0
f = reader(open("6452pol.csv"), delimiter=",", lineterminator="\"")
for i in f:
    d = {}
    for j in i:
        if j not in d.keys():
            d[j] = 1
        else:
            d[j] += 1

    if d[str(max(list(map(int, i))))] == 1:
        if len(set(d.values())) > 1:
            i = list(map(int, i))
            if (max(i) + min(i)) > (sum(i) - (max(i) + min(i))):
                c += 1
print(c)