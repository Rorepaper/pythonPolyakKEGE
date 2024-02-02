f = open("7626txt")
k = int(f.readline())
n = int(f.readline())
sp = []
for line in f:
    sp.append([int(line[0]), int(line[1])])

dic = {key: [] for key in range(1, k+1)}
kol = 0
for tur in sp:
    for key, val in dic.items():
        if not val or tur[0] > val[-1][1]:
            dic[key].append(tur)
print(dic)