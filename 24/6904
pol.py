f = open("6904\npol.txt").readline()
spp = []
for i in range(1, 10, 2):
    sp = f.split(str(i))
    for j in sp:
        if all(x in "AEIOUY" for x in j):
            spp.append(len(j))
print(max(spp))