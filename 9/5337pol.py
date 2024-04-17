from csv import reader
from itertools import permutations

c = 0
for i in reader(open("5337pol.csv")):
    i = list(map(int, i))
    if max(i) < sum(i) - max(i):
        for j in permutations(i):
            j = list(j)
            if j[0] + j[1] == j[2] + j[3]:
                c += 1
                break
print(c)
