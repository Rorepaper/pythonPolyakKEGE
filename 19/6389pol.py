def f(a, p):
    if a >= 73 or p < 0:
        return p % 2 == 0
    moves = [f(a + 1, p - 1), f(a + 3, p - 1), f(a * 2, p - 1)]

    return any(moves) if p % 2 else all(moves)


for n in range(20, 73):
    if not f(n, 2) and f(n, 4):
        print(n)
