f = open("8432.txt")
n = f.readline()

sp = []
for line in f:
    line = line.split()
    sp.append([int(line[0]), int(line[0]) + int(line[1]), line[2]])
sp.sort()

a = {key: [] for key in range(1, 71)}
b = {key: [] for key in range(1, 31)}
kolB = 0
kol = 0

for trans in sp:
    fl = False
    st = trans[0]
    end = trans[1]
    if trans[2] == "B":
        for key, val in b.items():
            if not val or val[-1] <= st:
                kolB += 1
                val.append(end)
                fl = True
                break
    else:
        for key, val in a.items():
            if not val or val[-1] <= st:
                val.append(end)
                fl = True
                break
        if not fl:
            for key, val in b.items():
                if not val or val[-1] <= st:
                    val.append(end)
                    fl = True
                    break
    if not fl:
        kol += 1

print(kolB, kol)
