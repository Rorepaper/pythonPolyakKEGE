f = open("4553.txt")
screen = [["-"] * 10000 for _ in range(10000)]

for line in f.readlines()[1:]:
    line = line.split()
    screen[int(line[0]) - 1][int(line[1]) - 1] = line[2]

podr = []

for i in range(len(screen)):
    s = "".join(screen[i])
    k = 0
    while "+" * (k + 1) in s:
        k += 1
    podr.append([k, i+1])
print(max(podr))
