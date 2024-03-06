def f(n):
    sp = []
    for d in range(10, 100):
        if n % d == 0:
            sp.append(d)
    return sp


for i in range(333555, 777999):
    sp = f(i)
    if len(sp) == 35:
        print(min(sp), max(sp))
