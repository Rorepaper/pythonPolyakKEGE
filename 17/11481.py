sp = list(map(int, open("/home/vidjakinra/Загрузки/17_11481.txt")))
sp8, sp2 = [], []

for i in sp:
    if str(abs(i))[0] == "8":
        sp8.append(i)
m8 = max(sp8)

for i in range(2, len(sp)):
    w = sp[i-2:i+1]
    c = 0
    for j in w:
        if str(abs(j))[0] == "6":
            c += 1
    if c <= 1 and sum(w) >= m8:
        sp2.append(sum(w))
print(len(sp2), min(sp2))
