def f(a, p):
    if a < 32 or p < 0:
        return p % 2 == 0

    moves = [f(a-3, p-1), f(a-2, p-1)]
    if a % 4 == 0:
        moves.append(f(a//4, p-1))

    if p % 2 == 1:
        return any(moves)
    else:
        return all(moves)


for s in range(32, 2000):
    if f(s, 2):
        print(s)