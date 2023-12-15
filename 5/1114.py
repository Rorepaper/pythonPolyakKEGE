for n in range(96, 1000):
    n2 = bin(n)[2:]

    for i in range(3):
        c0 = n2.count("0")
        c1 = n2.count("1")
        mini = min(c0, c1)
        if c0 == c1:
            n2 += n2[-1]
        else:
            if mini == c0:
                n2 += "0"
            else:
                n2 += "1"

    r = int(n2, 2)
    if r % 4 == 0:
        print(n)
        exit()

