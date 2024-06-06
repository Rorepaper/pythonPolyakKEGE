f = list(map(int, open("/home/vidjakinra/Загрузки/17-384.txt")))
c = 0
sp = []
spp = []
for i in range(1, len(f)):
    a, b = f[i-1:i+1]
    la, lb = len(str(a)), len(str(b))
    if (la == 2 and lb != 2) or (lb == 2 and la != 2):
        sp.append(a + b)

spm = max(sp)
print(spm)
for i in f:
    if i > spm:
        spp.append(i)
print(len(spp), min(spp))