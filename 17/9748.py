sp = list(map(int, open("/home/vidjakinra/Загрузки/17_9748.txt")))
sp15, sp2 = [[] for i in ".."]

for i in sp:
    if str(i)[-2:] == "15":
        sp15.append(i)
m15 = max(sp15)
for i in range(2, len(sp)):
    w = sp[i-2:i+1]
    c = 0
    for j in w:
        if len(str(j)) == 4:
            c += 1
    if c == 1 and sum(w) >= m15:
        sp2.append(sum(w))
print(len(sp2), max(sp2))
