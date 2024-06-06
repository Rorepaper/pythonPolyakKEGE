n = 7 * 729 ** 543 - 6 * 81 ** 765 - 5 * 9 ** 987 - 20
sp = []
while n:
    sp.append(n % 9)
    n //= 9
sp = sp[::-1]
print(sp.count(8))
