f = list(map(int, open("6517pol.txt").readlines()))
mini = float("inf")
sp = []
for i in f:
    if i % 2 == 0 and i < mini:
        mini = i

for i in range(2, len(f)):
    a, b, c = f[i-2:i+1]
    if any([a % 2, c % 2]) and not all([a % 2, c % 2]) and not b % mini:
        sp.append(a + c)

print(len(sp), min(sp))