for n in range(5, 51):
    n2 = bin(n)[2:]
    if sum(list(map(int, n2[:3]))) % 2 == 0:
        n2 = "1" + n2[:-2] + "01"
    else:
        n2 = "10" + n2[2:] + "1"
    r = int(n2, 2)
    if r > 50:
        print(n)
        exit()