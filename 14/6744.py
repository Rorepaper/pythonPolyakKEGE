for x in range(23):
    n1 = 7 * 23 ** 6 + x * 23 ** 5 + 3 * 23 ** 4 + 8 * 23 ** 3 + 5 * 23 ** 2 + 9 * 23 + 6
    n2 = 1 * 23 ** 4 + 4 * 23 ** 3 + x * 23 ** 2 + 3 * 23 + 6
    n3 = 6 * 23 ** 3 + 1 * 23 ** 2 + x * 23 + 7
    s = n1 + n2 + n3
    if s % 22 == 0:
        print(s // 22)