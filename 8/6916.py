from itertools import permutations
c = 0
for n in permutations("КОБУРА"):
    n = "".join(n)
    f = False
    for i in "КБР":
        for j in "КБР":
            if i+j in n:
                f = True
    for i in "ОУА":
        for j in "ОУА":
            if i+j in n:
                f = True
    if not f:
        c += 1

print(c)