f = open("8482.txt")
n = f.readline()
k = f.readline()

sp = []

for line in f.readlines():
    line = list(map(int, line.split()))
    sp.append([line[0], line[1]])

sp.sort()

a = {key: 419 for key in range(1, int(k) + 1)}
kol = 0


for time in range(7 * 60, 23 * 60 - 5):
    for i in sp:
        if i[0] == time:
            for key, val in a.items():
                if val <= time and time - val <= 10:
                    a[key] = i[1] + 5
                    print(key)
                    kol += 1
                    break
print(kol)



# for table in sp:
#     fl = False
#     sp1 = []
#     st = table[0]
#     end = table[1]
#     if end <= 23 * 60 - 5:
#         for key, val in a.items():
#             if not val or val[-1] <= st:
#                 val.append(end)
#                 fl = True
#                 kol += 1
#                 break
#             else:
#                 sp.append([val[-1] + 5 - st, key])
#         if not fl:
#             sp1.sort()
#             if sp[0][0] <= 10:
#                 a[sp1[0][1]].append(end + sp1[0][0])
#                 kol += 1
#
# print(kol)
