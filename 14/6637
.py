n = 7 * 5 ** 123 + 6 * 5 ** 111 - 5 * 25 ** 50 + 4 * 125 ** 30 - 3 * 5 ** 10
sp = []
while n:
    sp.append(str(n % 5))
    n //= 5
sp = "".join(sp[::-1])
print(sp.count("4"))
