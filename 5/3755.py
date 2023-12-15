res = []
for n in range(10, 444444):
    n1 = []
    n = str(n)
    for i in range(1, len(n)):
        n1.append(int(n[i - 1] + n[i]))
    r = max(n1) - min(n1)
    if r == 44:
        res.append(int(n))
print(min(res))
