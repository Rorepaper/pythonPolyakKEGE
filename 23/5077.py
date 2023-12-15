def f1(a, b, c, d):
    if a == b and d == 1:
        return 1
    if a > b or a > 20 or d == 0:
        return 0
    if a == 20:
        d = 1
    if c == 0:
        return f1(a + 1, b, 0, d) + f1(a + 3, b, 0, d) + f1(a * 2, b, 1, d)
    else:
        return f1(a + 1, b, 0, d) + f1(a + 3, b, 0, d)


print(f1(3, 60, 0, 0))
