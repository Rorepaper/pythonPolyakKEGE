from itertools import permutations
c = 0
for n in permutations("КОБУРА"):
    n = "".join(n)
    [n := n.replace(*i) for i in [("Б", "К"), ("Р", "К"), ("У", "О"), ("А", "О")]]
    if "ОО" not in n and "КК" not in n:
        c += 1
print(c)
