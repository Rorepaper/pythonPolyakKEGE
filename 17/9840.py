f = list(map(int, open("17.txt")))
ma = []
maa = []
for i in f:
    if str(i)[-2:] == "39" and 1000 <= abs(i) <= 9999:
        ma.append(i)

for i in range(1, len(f)):
    a = f[i - 1]
    b = f[i]
    if (len(str(abs(a))) == 4 and len(str(abs(b))) != 4) or (len(str(abs(a))) != 4 and len(str(abs(b))) == 4):
        if (a + b) ** 2 <= max(ma) ** 2:
            maa.append(a + b)

print(len(maa), max(maa))
