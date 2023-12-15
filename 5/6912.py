for n in range(1000, 10000):
    n8 = oct(n)[2:]
    for i in "0246":
        n8 = n8.replace(i, "1")
    n8 += str(n % 8)
    r = int(n8, 8)
    n8 = oct(r)[2:]
    for i in "0246":
        n8 = n8.replace(i, "1")
    n8 += str(n % 8)
    r = int(n8, 8)

    if r % 234 == 0:
        print(r)