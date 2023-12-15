def f(a, b, p, m):
    moves = []
    if a + b >= 100 or p < 0:
        return p % 2 == 0
    if m != 4:
        moves += [f(a*2, b, p-1, 4), f(a, b*2, p-1, 4)]

    for i in range(1, 4):
        moves.append(f(a+i, b, p-1, i))
        moves.append(f(a, b+i, p - 1, i))

    return any(moves) if p % 1 == 0 else all(moves)


for s in range(1, 98):
    if f(2, s, 3) and not f(2, s, 1):
        print(s)