sp, sp17, sp2 = list(map(int, open("/home/vidjakinra/Загрузки/17_9164.txt"))), [], []
for i in sp:
    if not i % 17:
        sp17.append(i)
m17 = max(sp17)
for i in range(1, len(sp)):
    print(sp[i-1:i+1])
    if sum(sp[i-1:i+1]) > m17:
        sp2.append(sum(sp[i-1:i+1]))
print(max(sp2), len(sp2))
