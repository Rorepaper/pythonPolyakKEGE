def f(a, b, p):
    if (a ** 2 + b ** 2) > 14 ** 2 or p < 0:
        return p % 2 == 0

    moves = [f(2 * a, b, p - 1), f(a, b + 3, p - 1), f(a, b + 4, p - 1)]

    return any(moves) if p % 2 == 1 else all(moves)


for s in range(1, 14):
    if f(3, s, 4) and not f(3, s, 2):
        print(s)
