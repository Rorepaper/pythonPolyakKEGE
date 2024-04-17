f = open("5253pol.txt").readline()
sp = f.split("2022")
spp = []
for i in range(3, len(sp)):
    spp.append(sum([len(y) for y in sp[i-4:i+1]]) + 4 * 4)
print(max(spp))
