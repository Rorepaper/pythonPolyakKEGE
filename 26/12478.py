f = open("12478.txt")
n, st, end = map(int, f.readline().split())
sp = []
sp1 = []
k = 0
for line in f.readlines():
    line = list(map(int, line.split()))
    sp.append(line)

sp.sort()

for i in range(1, len(sp)):
    if sp[i - 1][0] != sp[i][0]:
        sp1.append(sp[i])

fl = False
i = 0
while True:
    s1 = set(range(sp[i][0], sp[i][1]))
    if not fl:
        if st in s1:
            for j in range(len(sp), 0, -1):
                s2 = set(range(sp[j][0], sp[j][1]))
                if s1.intersection(s2):
                    i = j
                    k += 1
                    fl = True
    else:
        if end in s1:
            break

print(k)
