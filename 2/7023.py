from itertools import product
print("w x y z")
for w, x, y, z in product([0, 1], repeat=4):
    f = not((((not w) <= (not y)) <= (not z)) <= x)
    if f:
        print(w, x, y, z)
