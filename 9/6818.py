from csv import reader
f = reader(open("/home/vidjakinra/Загрузки/9-226.csv"), delimiter=",", lineterminator="\"")
for i in f:
    i = list(map(int, i))
    d = {}
    for j in i:
        if str(j) not in d.keys():
            d[str(j)] = 1
        else:
            d[str(j)] += 1
    print(d)
    if list(d.values()).count(2) == 2:
        if d[str(max(i))] != 2:
            print(sum(i))
