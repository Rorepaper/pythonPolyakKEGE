for a1 in range(1, 1000):
    for a2 in range(1, 1000):
        a = range(a1, a2)
        if all(((x in a) <= (x ** 2 <= 100)) and ((x ** 2 <= 64) <= (x in a)) for x in range(1, 1000)):
            print(len(a))
