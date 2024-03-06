from itertools import permutations

# def pr(n):
#     for d in range(2, int(n ** 0.5) + 1):
#         if n % d == 0:
#             return False
#     return True
#
#
#
# sp = []
# for i in range(1, 529679):
#     if pr(i):
#         sp.append(i)
# print(sp)
a = list(map(int, open("680.txt").readline()[1:-1].split(", ")))


for x in range(len(a) - 2):
    if a[x] * a[x + 1] * a[x + 2] > 529678:
        break
    for y in range(x + 1, len(a) - 1):
        for z in range(y + 1, len(a)):
            if a[z] - a[x] >= 100:
                break
            if 485617 <= a[x] * a[y] * a[z] <= 529678:
                if str(a[x])[-1] == str(a[y])[-1] == str(a[z])[-1]:
                    print(a[x] * a[y] * a[z], a[z] - a[x])

