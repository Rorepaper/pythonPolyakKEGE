from itertools import product
c = 0
for i in product("ВЕБИНАР", repeat=7):
    if len(set(i)) == 7:
        f = False
        i = "".join(i)
        for j in "ВБНР":
            for k in "ВБНР":
                if j + k in i:
                    f = True
        for j in "ЕИА":
            for k in "ЕИА":
                if j + k in i:
                    f = True
        if not f:
            c += 1
print(c)