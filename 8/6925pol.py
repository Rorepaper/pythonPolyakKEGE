from itertools import product

c = 0
for s in product("ВАСЯ", repeat=5):
    s = "".join(s)
    if s.count("А") >= 1:
        c += 1
print(c)