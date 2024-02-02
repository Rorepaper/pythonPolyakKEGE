f = list(map(int, open("6488pol.txt")))

maxi = 0
sp = []

for i in f:
    if 100 <= abs(i) <= 999 and str(sum(map(int, str(abs(i)))))[-1] == "3":
        if i > maxi:
            maxi = i

for i in range(1, len(f)):
    a, b = f[i-1:i+1]
    la, lb = [len(str(abs(x))) for x in [a, b]]
    if (la == 4 and lb != 4) or (la != 4 and lb == 4):
        if (a ** 2 + b ** 2) % maxi == 0:
            sp.append(a ** 2 + b ** 2)
print(len(sp), max(sp))