f = list(map(int, open("/home/vidjakinra/Загрузки/17-385.txt")))

sp = []

for i in f:
    sp.append(sum(list(map(int, list(str(i))))))
spm = max(sp)

sp = []

for i in range(1, len(f)):
    a, b = f[i-1:i+1]
    spp = []
    if a + b > 2 * spm:
        for j in a, b:
            spp.append(sum(list(map(int, list(str(i))))))
        sp.append(sum(spp))
print(len(sp), max(sp))