def f(n):
    if n == 1:
        return 1
    elif n > 1:
        return f(n - 1) + n

print(f(40))
