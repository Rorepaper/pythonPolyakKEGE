from csv import reader
f = reader(open("/home/vidjakinra/Загрузки/9-227.csv"), delimiter=",", lineterminator="\"")
c = 0
for i in f:
    i = list(map(int, i))
    i.sort()
    if len(set(i)) == 3:
        if (i[2] + i[3])/2 > (i[0] + i[1]):
            if i[3] % i[0] != 0:
                c += 1
print(c)
