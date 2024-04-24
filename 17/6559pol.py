f = list(map(int, open("6559pol.txt").readlines()))
mini = float("inf")
sp = []
for i in f:
    if len(str(i)) == 3 and len(set(str(i))) == 3 and i < mini:
        mini = i

for i in range(1, len(f)//2 + 1):
    a, b = f[i-1], f[-i]
    if a * b % mini == 0:
        sp.append(a+b)
print(len(sp), min(sp))