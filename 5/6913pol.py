c = 0
for n in range(10000, 99999):
    n8 = oct(n)[2:]
    for i in "1357":
        n8 = n8.replace(i, "2")
    n8 += str(n % 8)

    n8 = oct(int(n8, 8))[2:]

    for i in "1357":
        n8 = n8.replace(i, "2")
    n8 += str(n % 8)
    r = int(n8, 8)
    if r % 2023 == 0:
        c += n
print(c)