f = open("6680\npol.txt").readline()
c = 0
sp = f.split("#")
for i in sp:
    col = i[:6]
    if len(col) == 6:
        try:
            int(col, 16)
            r, g, b = [int(col[x-1:x+1], 16) for x in range(1, len(col), 2)]
            if r > g and r > b:
                c += 1
        except IndentationError:
            continue
print(c)
