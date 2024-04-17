sp = []
for x in range(23):
    s = 0
    for j in ["7x38596", "14x36", "61x7"]:
        for n in range(len(j)):
            s += (x if j[n] == "x" else int(j[n])) * 23 ** (len(j)-n-1)
    if s % 22 == 0:
        sp.append(s // 22)
print(min(sp))
