f = open("4369\n.txt")
hall = [["-"] * 25000 for _ in range(25000)]
for line in f.readlines()[1:]:
    line = list(map(int, line.split()))
    hall[line[0]-1][line[1]-1] = str(line[2])

podr = []

for i in range(len(hall)):
    s = "".join(hall[i])
    k = s.count("1")
    if k >= 500:
        if "-" * 100 in s:
            spl = s.split("-" * 100)
            spl1 = []
            for x in spl:
                if x:
                    spl1.append(x)
            for j in range(1, len(spl1)):
                if spl1[j - 1][-1] == "1" and spl1[j][0] == "1":
                    podr.append([i + 1, k])
print(max(podr))
