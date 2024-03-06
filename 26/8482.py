f = open("8482.txt")
n = f.readline()
k = f.readline()

sp = []

for line in f.readlines():
    line = list(map(int, line.split()))
    sp.append([line[0], line[1]])

sp.sort()

a = {key: 419 for key in range(1, int(k) + 1)}
kol = 0


for time in range(7 * 60, 23 * 60 - 5):
    for i in sp:
        if i[0] == time:
            for key, val in a.items():
                if val <= time and time - val <= 10:
                    a[key] = i[1] + 5
                    print(key)
                    kol += 1
                    break
print(kol)



