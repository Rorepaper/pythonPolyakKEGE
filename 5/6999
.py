for n in range(1, 1000):
    n2 = bin(n)[2:]
    n2st = n2[:2]
    n2 = n2[::-1]
    ind = n2.find("0")
    if ind:
        n2 = n2.replace(n2[ind], n2st[::-1])
    else:
        n2 = "0"
    r = int(n2, 2)
    if r == 123:
        print(n)
