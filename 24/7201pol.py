a = open("7201pol.txt").readline().replace("A", "C").replace("B", "C").split("C")
sp = []
for i in range(len(a)):
    x, y, z = [a[i].count(j) for j in ("X", "Y", "Z")]
    if x == 5 and y == 5 and z == 5:
        sp.append(len(a[i]))
    else:
        for j in range(len(a[i]) - 1):
            for jj in range(j+1, len(a[i])):
                if a[i][j:jj].count("X") > 5 or a[j][j:jj].count("Y") > 5 or a[j][j:jj].count("Z") > 5:
                    sp.append(len(a[i][j:jj]))
print(max(sp))
