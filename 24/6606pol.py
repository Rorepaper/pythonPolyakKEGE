import re
a = open("6606pol.txt").readline().replace("EA", "*").replace("NPC", "-")
num = re.findall(r'[*-]+|\d+', a)
sp = []
c = 0
for i in sorted(num, key=lambda x: len(x))[-1]:
    c += 2 if i == "*" else 3
print(c)
