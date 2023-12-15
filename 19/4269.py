def f(a, b, p):
    if a + b >= 150 or p < 0:
        return p % 2 == 0

    hodi = [f(a+1, b, p-1), f(a, b+1, p-1), f(a+2, b, p-1), f(a, b+2, p-1), f(a+b, b, p-1), f(a, a+b, p-1)]

    if p % 2 == 1:
        return any(hodi)
    else:
        return all(hodi)


for s in range(1, 89):
    if f(61, s, 2):
        print(s)