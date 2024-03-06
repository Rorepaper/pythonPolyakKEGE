f = open("7826.txt")
k, n = map(int, f.readline().split())

sp = []

for line in f.readlines():
    line = list(map(int, line.split()))
    sp.append([line[0], line[1]])

sp.sort()

a = {key: [-1] for key in range(1, int(k) + 1)}
kol = 0
fl = True

d = {}

for i in range(len(sp)):
    if sp[i][0] not in d.keys():
        d[sp[i][0]] = [1, sp[i][1]]
    else:
        d[sp[i][0]][0] += 1
        d[sp[i][0]][1] = sp[i][1]


for k1, val1 in d.items():
    for k, val in a.items():
        if val[-1] < k1:
            a[k].append(val1[1])
            kol += val1[0]
            print(k)
            break

print(kol)

