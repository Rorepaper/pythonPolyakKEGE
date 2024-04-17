def f(x, a):
    return (not(x in a)) <= (not(x in {1, 12}) and not(x in (range(12, 17))))

a = []
for x in range(1, 1000):
    if not f(x, a):
        a.append(x)
print(a)