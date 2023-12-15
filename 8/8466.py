from itertools import product
sp = []
c = 0
for n in product("0123456", repeat=6):
    c += 1
    n = "".join(n)

    if n[0] != "0" and int(n[-1]) >= 4:
        ch = nch = 0
        for i in n:
            if i in "0246":
                ch += 1
        if ch == 3:
            sp.append([c, n])
print(len(sp))
