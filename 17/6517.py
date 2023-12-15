f = list(map(int, open("/home/vidjakinra/Загрузки/17-374.txt")))
sp = []
mini = 0
for i in sorted(f):
    if i % 2 == 0:
        mini = i
        break

for i in range(1, len(f) - 1):
    a = f[i-1:i+2]
    chet = []
    for j in a[0], a[2]:
        if j % 2 == 0:
            chet.append(j)
    if len(chet) == 1:
        if a[1] % mini == 0:
            sp.append(a[0] + a[2])
print(len(sp), min(sp))
