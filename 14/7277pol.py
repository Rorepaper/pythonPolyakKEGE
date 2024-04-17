from itertools import product

for osn in range(10, 100):
    for x, y, z, w in product(range(osn), repeat=4):
        a1 = 9 + x * osn + y * osn ** 2 + x * osn ** 3 + z * osn ** 4
        a1 += 8 + 4 * osn + 7 * osn ** 2 + y * osn ** 3 + x * osn ** 4
        a2 = 1 + 6 * osn + x * osn ** 2 + z * osn ** 3 + w * osn ** 4
        if a1 == a2:
            print(w + z * osn + y * osn ** 2 + x * osn ** 3)
            break
