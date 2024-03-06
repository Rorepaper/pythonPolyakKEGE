for a in range(1000):
    if all(((x % 10 == 0) and (x % 26 == 0) and (x >= 300)) <= (a <= x) for x in range(1000)):
        print(a)