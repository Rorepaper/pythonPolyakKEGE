import re

a = open("6650pol.txt").readline()
let = re.findall(r'([A-Z]+|\d+,[0-9]+|\d+)', a)
num = re.findall(r'[0-9]+|\d+', a)
sp = []
print(let)
exit()
for i in range(len(let)):
    sp.append(let[i])
    try:
        sp.append(num[i])
    except IndexError:
        continue
spp = []



print(sorted(sp, key=lambda x: len(x)))
