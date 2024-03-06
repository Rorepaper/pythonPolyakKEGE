from csv import reader
from itertools import permutations


f = reader(open("6627pol.csv"), delimiter=";")
c = 0
for i in f:
    i = list(map(int, i))
    if (min(i) + max(i)) % 3 == 0:
        for j in permutations(i, r=4):
            j = list(j)
            if j[1] - j[0] == j[3] - j[2]:
                c += 1
                break
print(c)
print(2 ** 8)