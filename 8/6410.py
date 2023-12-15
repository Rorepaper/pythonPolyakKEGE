from itertools import product
sp = []
c = 0

for n in product("ГАЛКТИ", repeat=8):
    n = "".join(n)
    if n[0] in "ГЛКТ" and n[-1] in "АИ":
        f = False
        for i in range(1, len(n)):
            if (ord(n[i]) - ord(n[i-1])) == 1:
                f = True
        if not f:
            c += 1
print(c)
