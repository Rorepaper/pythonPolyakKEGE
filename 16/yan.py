def f(n):
    if n <= 1:
        return 1/2
    else:
        if (n + 1) * f(n - 1) == int((n + 1) * f(n - 1)):
            return int((n + 1) * f(n - 1))
        return (n + 1) * f(n - 1)


# print(f(200)/f(198))

d = {}

for n in range(1, 201):
    if n <= 1:
        d[n] = 1/2
    else:
        if (n + 1) * d[n - 1] == int((n + 1) * d[n - 1]):
            d[n] = int((n + 1) * d[n - 1])
        else:
            d[n] = (n + 1) * d[n - 1]

print(d[200] / d[198])
