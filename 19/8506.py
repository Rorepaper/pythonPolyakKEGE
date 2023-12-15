def f(a, b, p):
    if a + b > 342 or p < 0:
        return p % 2 == 0
    hodi = [f(a + 2, b, p - 1), f(a, b + 2, p - 1), f(a * 5, 0, p - 1), f(a, b * 5, p - 1)]
    if p % 2 == 1:
        return any(hodi)
    else:
        return all(hodi)


for s in range(1, 326):
    if f(11, s, 3) and not f(11, s, 1):
        print(s)
