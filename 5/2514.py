for n in range(100000, 1000000):
    n2 = str(n)
    a10 = 0
    if n2[-2] == "9" and "2" in n2:
        a1 = ""
        for i in range(0, len(n2), 2):
            a1 += str(int(n2[i]) + int(n2[i + 1]))
        a2 = bin(int(a1))[2:]
        a2 += "0" if int(a1) % 2 == 0 else "1"
        a10 = int(a2, 2)
    if a10 == 1519:
        print(n)
        break

