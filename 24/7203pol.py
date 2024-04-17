a = open("7203pol.txt").readline()
sp = a.replace("Y", "X").split("X")
spp = []
for i in sp:
    s, u, n = i.count("S"), i.count("U"), i.count("N")
    if s <= 10 and u <= 10 and n <= 10:
        # spp.append(len(i))
        continue
    else:
        print(i)
        for j in "S", "U", "N":
            if i.count(j) > 10:
                i.split("S")
                for x in range(len(i)):
                    if len(i) - x > 10:
                        spr = i[x:10]
                    else:
                        spr = i[x:len(i)]
                    spp.append(len(spr))

print(max(spp))
