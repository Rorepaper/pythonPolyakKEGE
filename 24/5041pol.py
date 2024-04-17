f = open("5041pol.txt").readline()
sp = []
for i in range(len(f)-2):
    j = i
    while j < len(f) - 2:
        if (f[j] == "X" or f[j] == "Z") and f[j+2] == "Y":
            j += 3
        else:
            sp.append((j-i)//3)
            break
print(max(sp))