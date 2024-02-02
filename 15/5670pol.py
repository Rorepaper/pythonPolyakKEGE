c = 0
for a in range(1, 10000):
    if all(((x % 12 == 0) and (70 <= x <= 80) and (not(x % a == 0))) == 0 for x in range(1, 10000)):
        c += 1
print(c)