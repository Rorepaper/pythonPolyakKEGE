f = open("7096.txt")
n = int(f.readline())
sp = list(map(int, f))
sp.sort(reverse=True)
box = sp[0]
c = 1
for i in sp[1:]:
    if box - i >= 11:
        box = i
        c += 1
print(c, box)