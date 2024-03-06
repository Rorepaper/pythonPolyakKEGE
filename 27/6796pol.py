f = open("6796pol.txt")
n, k = map(int, f.readline().split())
spp = []
sp = list(map(int, f.readlines()))
for i1 in range(len(sp) - 2 * k):
    for i2 in range(i1 + k, len(sp) - k):
        for i3 in range(i2 + k, len(sp)):
            spp.append(sp[i1] + sp[i2] + sp[i3])
print(max(spp))


# for i1 in range(len(sp) - 2):
#     for i2 in range(i1 + 1, len(sp) - 1):
#         for i3 in range(i2 + 1, len(sp)):
#             if i3 - i2 >= k and i2 - i1 >= k:
#                 spp.append(sp[i1] + sp[i2] + sp[i3])
# print(max(spp))
