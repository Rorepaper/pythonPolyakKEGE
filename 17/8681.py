f = list(map(int, open("8681")))
keys, res = [], []
for i in f:
    if 1000 <= i <= 9999 and str(i)[-1] == "7":
        keys.append(i)

key = min(keys)

for i in range(1, len(f)):
    a, b = f[i-1:i+1]
    if len(str(a)) == 4 or len(str(b)) == 4:
        if ((a * b) % key) == 0:
            res.append(a * b)
print(len(res), max(res))
