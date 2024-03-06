f = list(map(int, open("40733resh.txt")))

sp = []
ch = []

for i in f:
    if i % 2 == 0:
        ch.append(i)
sr = sum(ch) / len(ch)

for i in range(1, len(f)):
    a, b = f[i-1:i+1]
    if a % 3 == 0 or b % 3 == 0:
        if (a < sr) or (b < sr):
            sp.append(a + b)
print(len(sp), max(sp))