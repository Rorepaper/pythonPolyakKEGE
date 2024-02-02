for n in range(1, 1000000000):
    su = sum(range(len(str(n)) + 1))
    if n == 123456789:
        print(su)
    n2 = bin(su)[2:]
    ed = n2.count("1")
    if ed % 2 == 0:
        n2 = "1" + n2 + "00"
    else:
        n2 = "10" + n2 + "1"
    r = int(n2, 2)
    if r == 21:
        print(n)

# Ответ: 9