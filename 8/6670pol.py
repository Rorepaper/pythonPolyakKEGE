from itertools import product

sp = []
for n in product("ЛИСЁНОК", repeat=5):
    n = "".join(n)
    sp.append(n)
sp.sort()
for i in range(len(sp)):
    n = sp[i]
    if n.count("Ё") >= 2 and n[0] != "О" and n[1] == "К":
        print(i + 1)
