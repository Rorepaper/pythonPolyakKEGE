from itertools import product
c = 0
for n in product("0123", repeat=4):
    n = "".join(n)
    if n[0] != "0":
        d = {}
        for i in n:
            if i not in d.keys():
                d[i] = 1
            else:
                d[i] += 1
        if max(list(d.values())) >= 2:
            c += 1
print(c)