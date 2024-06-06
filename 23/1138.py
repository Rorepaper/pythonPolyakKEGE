def f1(a, b):
    if a == b:
        return 1
    if a < b:
        return 0
    else:
        return f1(bin(int(a, 2) - 1)[2:], b) + f1(a[:-1], b)


print(f1("100001", "100"))
